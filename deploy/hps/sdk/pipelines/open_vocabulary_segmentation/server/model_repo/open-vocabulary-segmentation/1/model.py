import numpy as np
import pycocotools.mask as mask_util
from paddlex_hps_server import BaseTritonPythonModel, schemas, utils


def _rle(mask: np.ndarray) -> str:
    rle_res = mask_util.encode(np.asarray(mask[..., None], order="F", dtype="uint8"))[0]
    return rle_res["counts"].decode("utf-8")


class TritonPythonModel(BaseTritonPythonModel):
    def get_input_model_type(self):
        return schemas.open_vocabulary_segmentation.InferRequest

    def get_result_model_type(self):
        return schemas.open_vocabulary_segmentation.InferResult

    def run(self, input, log_id):
        file_bytes = utils.get_raw_bytes(input.image)
        image = utils.image_bytes_to_array(file_bytes)
        visualize_enabled = input.visualize if input.visualize is not None else self.app_config.visualize

        result = list(
            self.pipeline.predict(
                image,
                prompt=input.prompt,
                prompt_type=input.promptType,
            )
        )[0]

        rle_masks = [
            dict(rleResult=_rle(mask), size=mask.shape) for mask in result["masks"]
        ]
        mask_infos = result["mask_infos"]
        if visualize_enabled:
            output_image_base64 = utils.base64_encode(
                utils.image_to_bytes(result.img["res"])
            )
        else:
            output_image_base64 = None

        return schemas.open_vocabulary_segmentation.InferResult(
            masks=rle_masks, maskInfos=mask_infos, image=output_image_base64
        )
