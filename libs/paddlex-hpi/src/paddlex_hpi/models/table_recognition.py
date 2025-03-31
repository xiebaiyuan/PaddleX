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

import tempfile
from typing import Any, Dict, List

import numpy as np
import ultra_infer as ui
from paddlex_hpi._utils.compat import get_compat_version
from paddlex_hpi.models.base import CVPredictor

from paddlex.inference.common.batch_sampler import ImageBatchSampler
from paddlex.inference.models.table_structure_recognition.result import TableRecResult
from paddlex.modules.table_recognition.model_list import MODELS


class TablePredictor(CVPredictor):
    entities = MODELS

    def _build_ui_model(
        self, option: ui.RuntimeOption
    ) -> ui.vision.ocr.StructureV2Table:
        compat_version = get_compat_version()
        if compat_version == "2.5" or self.model_name == "SLANet":
            bbox_shape_type = "ori"
        else:
            bbox_shape_type = "pad"
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt") as f:
            pp_config = self.config["PostProcess"]
            for lab in pp_config["character_dict"]:
                f.write(lab + "\n")
            f.flush()
            model = ui.vision.ocr.StructureV2Table(
                str(self.model_path),
                str(self.params_path),
                table_char_dict_path=f.name,
                box_shape=bbox_shape_type,
                runtime_option=option,
            )
        return model

    def _build_batch_sampler(self) -> ImageBatchSampler:
        return ImageBatchSampler()

    def _get_result_class(self) -> type:
        return TableRecResult

    def process(self, batch_data: List[Any]) -> Dict[str, List[Any]]:
        batch_raw_imgs = self._data_reader(imgs=batch_data.instances)
        imgs = [np.ascontiguousarray(img) for img in batch_raw_imgs]
        ui_results = self._ui_model.batch_predict(imgs)

        bbox_list = []
        structure_list = []
        structure_score_list = []
        for ui_result in ui_results:
            bbox_list.append(ui_result.table_boxes)
            structure_list.append(ui_result.table_structure)
            structure_score_list.append(0.0)

        return {
            "input_path": batch_data.input_paths,
            "page_index": batch_data.page_indexes,
            "input_img": batch_raw_imgs,
            "bbox": bbox_list,
            "structure": structure_list,
            "structure_score": structure_score_list,
        }
