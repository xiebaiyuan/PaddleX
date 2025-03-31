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

import os
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import ultra_infer as ui
from paddlex_hpi.models.base import CVPredictor, HPIParams
from pydantic import BaseModel

from paddlex.inference.common.batch_sampler import ImageBatchSampler
from paddlex.inference.models.object_detection.result import DetResult
from paddlex.modules.object_detection.model_list import MODELS
from paddlex.utils import logging


class _DetPPParams(BaseModel):
    threshold: float
    label_list: List[str]


class DetPredictor(CVPredictor):
    entities = MODELS

    def __init__(
        self,
        model_dir: Union[str, os.PathLike],
        config: Optional[Dict[str, Any]] = None,
        device: Optional[str] = None,
        batch_size: int = 1,
        hpi_params: Optional[HPIParams] = None,
        img_size: Optional[Union[int, Tuple[int, int]]] = None,
        threshold: Optional[float] = None,
        layout_nms: Optional[bool] = None,
        layout_unclip_ratio: Optional[Union[float, Tuple[float, float]]] = None,
        layout_merge_bboxes_mode: Optional[str] = None,
    ) -> None:
        super().__init__(
            model_dir=model_dir,
            config=config,
            device=device,
            batch_size=batch_size,
            hpi_params=hpi_params,
        )
        self._pp_params = self._get_pp_params()
        self._threshold = threshold or self._pp_params.threshold

        unsupported_params = {
            "img_size": img_size,
            "layout_nms": layout_nms,
            "layout_unclip_ratio": layout_unclip_ratio,
            "layout_merge_bboxes_mode": layout_merge_bboxes_mode,
        }
        for param_name, param_value in unsupported_params.items():
            if param_value:
                logging.warning(
                    f"`{param_name}` is not supported for multilabel classification in PaddleX HPI"
                )

    def _build_ui_model(
        self, option: ui.RuntimeOption
    ) -> ui.vision.detection.PaddleDetectionModel:
        model = ui.vision.detection.PaddleDetectionModel(
            str(self.model_path),
            str(self.params_path),
            str(self.config_path),
            runtime_option=option,
        )
        return model

    def _build_batch_sampler(self) -> ImageBatchSampler:
        return ImageBatchSampler()

    def _get_result_class(self) -> type:
        return DetResult

    def process(
        self,
        batch_data: List[Any],
        img_size: Optional[Union[int, Tuple[int, int]]] = None,
        threshold: Optional[float] = None,
        layout_nms: Optional[bool] = None,
        layout_unclip_ratio: Optional[Union[float, Tuple[float, float]]] = None,
        layout_merge_bboxes_mode: Optional[str] = None,
    ) -> Dict[str, List[Any]]:
        unsupported_params = {
            "img_size": img_size,
            "layout_nms": layout_nms,
            "layout_unclip_ratio": layout_unclip_ratio,
            "layout_merge_bboxes_mode": layout_merge_bboxes_mode,
        }
        for param_name, param_value in unsupported_params.items():
            if param_value:
                logging.warning(
                    f"`{param_name}` is not supported for multilabel classification in PaddleX HPI"
                )

        batch_raw_imgs = self._data_reader(imgs=batch_data.instances)
        imgs = [np.ascontiguousarray(img) for img in batch_raw_imgs]
        threshold = threshold or self._threshold
        ui_results = self._ui_model.batch_predict(imgs)

        boxes_list = []
        for ui_result in ui_results:
            inds = sorted(
                range(len(ui_result.scores)),
                key=ui_result.scores.__getitem__,
                reverse=True,
            )
            inds = [i for i in inds if ui_result.scores[i] > threshold]
            inds = [i for i in inds if ui_result.label_ids[i] > -1]
            ids = [ui_result.label_ids[i] for i in inds]
            scores = [ui_result.scores[i] for i in inds]
            boxes = [ui_result.boxes[i] for i in inds]
            boxes = [
                {
                    "cls_id": id_,
                    "label": self._pp_params.label_list[id_],
                    "score": score,
                    "coordinate": box,
                }
                for id_, score, box in zip(ids, scores, boxes)
            ]
            boxes_list.append(boxes)

        return {
            "input_path": batch_data.input_paths,
            "page_index": batch_data.page_indexes,
            "input_img": batch_raw_imgs,
            "boxes": boxes_list,
        }

    def _get_pp_params(self) -> _DetPPParams:
        return _DetPPParams(
            threshold=self.config["draw_threshold"],
            label_list=self.config["label_list"],
        )
