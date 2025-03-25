# copyright (c) 2024 PaddlePaddle Authors. All Rights Reserve.
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

from pathlib import Path

import PIL
from PIL import ImageFont
from .. import logging
from ..download import download


def get_font_file_path(file_name: str) -> str:
    """
    Get the path of the font file.

    Returns:
    str: The path to the font file.
    """
    font_path = (Path(__file__).parent / file_name).resolve().as_posix()
    if not Path(font_path).exists():
        download(
            url=f"https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/fonts/{file_name}",
            save_path=font_path,
        )

    return font_path


def create_font(txt: str, sz: tuple, font_path: str) -> ImageFont:
    """
    Create a font object with specified size and path, adjusted to fit within the given image region.

    Parameters:
    txt (str): The text to be rendered with the font.
    sz (tuple): A tuple containing the height and width of an image region, used for font size.
    font_path (str): The path to the font file.

    Returns:
    ImageFont: An ImageFont object adjusted to fit within the given image region.
    """

    font_size = int(sz[1] * 0.8)
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    if int(PIL.__version__.split(".")[0]) < 10:
        length = font.getsize(txt)[0]
    else:
        length = font.getlength(txt)

    if length > sz[0]:
        font_size = int(font_size * sz[0] / length)
        font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    return font


PINGFANG_FONT_FILE_PATH = get_font_file_path("PingFang-SC-Regular.ttf")
SIMFANG_FONT_FILE_PATH = get_font_file_path("simfang.ttf")
