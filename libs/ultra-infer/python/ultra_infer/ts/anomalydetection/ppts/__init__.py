# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import os
from copy import deepcopy
import numpy as np
from typing import List
from dataclasses import dataclass

from .... import UltraInferModel, ModelFormat
from ....py_only.ts import PyOnlyTSModel
from ....utils.misc import load_config
from ....py_only import PyOnlyProcessorChain
from ....py_only.ts import PyOnlyTSModel, processors as P


class PyOnlyAnomalyDetectionModel(PyOnlyTSModel):
    def __init__(
        self,
        model_file,
        params_file,
        config_file,
        scaler_file=None,
        runtime_option=None,
        model_format=ModelFormat.PADDLE,
    ):
        self._model_file = model_file
        self._params_file = params_file
        self._model_format = model_format
        super().__init__(runtime_option)
        if scaler_file is None:
            config_dir = os.path.dirname(config_file)
            scaler_file = os.path.join(config_dir, "scaler.pkl")
        self._config = load_config(config_file)
        self._preprocessor = _PyOnlyAnomalyDetectionPreprocessor(
            self._config, scaler_file
        )
        self._postprocessor = _PyOnlyAnomalyDetectionPostprocessor(self._config)

    def model_name():
        return "PyOnlyAnomalyDetectionModel"

    def batch_predict(self, ts_list):
        data_list = []
        for csv_data in ts_list:
            data = {"ori_ts": deepcopy(csv_data), "ts": csv_data}
            data = self._preprocessor.run(data)
            data_list.append(data)

        input_data = {}
        input_num = self._runtime.num_inputs()
        for idx in range(input_num):
            input_name = self._runtime.get_input_info(idx).name
            ts_data = np.stack(
                [data["ts"][idx] for data in data_list], axis=0, dtype=np.float32
            )
            ts_data = np.ascontiguousarray(ts_data)
            input_data[input_name] = ts_data

        output_arrs = self._runtime.infer(input_data)

        results = []
        for idx, data in enumerate(output_arrs[0]):
            data = {"ori_ts": data_list[idx]["ori_ts"], "pred": data}
            result = self._postprocessor.run(data)
            results.append(result)
        return results

    def _update_option(self):
        self._option.set_model_path(
            self._model_file, self._params_file, self._model_format
        )


class _PyOnlyAnomalyDetectionPreprocessor(object):
    def __init__(self, config, scaler_file):
        super().__init__()
        self.scaler_file = scaler_file
        processors = self._build_processors(config)
        self._processor_chain = PyOnlyProcessorChain(processors)

    def run(self, data):
        return self._processor_chain(data)

    def _build_processors(self, config):
        processors = []
        processors.append(P.CutOff(config["size"]))

        if config.get("scale", None):
            if not os.path.exists(self.scaler_file):
                raise Exception(f"Cannot find scaler file: {self.scaler_file}")
            processors.append(P.Normalize(self.scaler_file, config["info_params"]))

        processors.append(P.BuildTSDataset(config["info_params"]))

        if config.get("time_feat", None):
            processors.append(
                P.CalcTimeFeatures(
                    config["info_params"],
                    config["size"],
                    config["holiday"],
                )
            )

        processors.append(P.DataFrame2Arrays(config["input_data"]))
        return processors


class _PyOnlyAnomalyDetectionPostprocessor(object):
    def __init__(self, config):
        super().__init__()
        self.model_threshold = config["model_threshold"]
        self.info_params = config["info_params"]

    def run(self, data):
        ori_ts = data["ori_ts"]
        pred = data["pred"]
        if ori_ts.get("past_target", None) is not None:
            ts = ori_ts["past_target"]
        elif ori_ts.get("observed_cov_numeric", None) is not None:
            ts = ori_ts["observed_cov_numeric"]
        elif ori_ts.get("known_cov_numeric", None) is not None:
            ts = ori_ts["known_cov_numeric"]
        elif ori_ts.get("static_cov_numeric", None) is not None:
            ts = ori_ts["static_cov_numeric"]
        else:
            raise ValueError("No value in ori_ts")
        column_name = (
            self.info_params["target_cols"]
            if "target_cols" in self.info_params
            else self.info_params["feature_cols"]
        )

        anomaly_score = np.mean(np.square(pred - np.array(ts)), axis=-1)
        anomaly_label = (anomaly_score >= self.model_threshold) + 0

        past_target_index = ts.index
        past_target_index.name = self.info_params["time_col"]

        label = anomaly_label.tolist()
        dates = past_target_index.tolist()
        col_names = ["label"]
        data = [label]
        result = _PyOnlyAnomalyDetectionResult(
            dates=dates, col_names=col_names, data=data
        )
        return result


@dataclass
class _PyOnlyAnomalyDetectionResult(object):
    dates: List[int]
    col_names: List[str]
    data: List[List[int]]
