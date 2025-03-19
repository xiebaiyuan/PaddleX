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
from __future__ import annotations

import copy
from pathlib import Path
from PIL import Image, ImageDraw

import re
import numpy as np
from PIL import Image
from PIL import ImageDraw

from ...common.result import (
    BaseCVResult,
    HtmlMixin,
    JsonMixin,
    MarkdownMixin,
    XlsxMixin,
)
from .utils import get_layout_ordering
from .utils import get_show_color


class LayoutParsingResultV2(BaseCVResult, HtmlMixin, XlsxMixin, MarkdownMixin):
    """Layout Parsing Result V2"""

    def __init__(self, data) -> None:
        """Initializes a new instance of the class with the specified data."""
        super().__init__(data)
        HtmlMixin.__init__(self)
        XlsxMixin.__init__(self)
        MarkdownMixin.__init__(self)
        JsonMixin.__init__(self)
        self.title_pattern = self._build_title_pattern()

    def _build_title_pattern(self):
        # Precompiled regex pattern for matching numbering at the beginning of the title
        numbering_pattern = (
            r"(?:"
            + r"[1-9][0-9]*(?:\.[1-9][0-9]*)*[\.、]?|"
            + r"[\(\（](?:[1-9][0-9]*|["
            r"一二三四五六七八九十百千万亿零壹贰叁肆伍陆柒捌玖拾]+)[\)\）]|" + r"["
            r"一二三四五六七八九十百千万亿零壹贰叁肆伍陆柒捌玖拾]+"
            r"[、\.]?|" + r"(?:I|II|III|IV|V|VI|VII|VIII|IX|X)\.?" + r")"
        )
        return re.compile(r"^\s*(" + numbering_pattern + r")(\s*)(.*)$")

    def _get_input_fn(self):
        fn = super()._get_input_fn()
        if (page_idx := self["page_index"]) is not None:
            fp = Path(fn)
            stem, suffix = fp.stem, fp.suffix
            return f"{stem}_{page_idx}{suffix}"
        else:
            return fn

    def _to_img(self) -> dict[str, np.ndarray]:
        res_img_dict = {}
        model_settings = self["model_settings"]
        if model_settings["use_doc_preprocessor"]:
            for key, value in self["doc_preprocessor_res"].img.items():
                res_img_dict[key] = value
        res_img_dict["layout_det_res"] = self["layout_det_res"].img["res"]

        if model_settings["use_general_ocr"] or model_settings["use_table_recognition"]:
            res_img_dict["overall_ocr_res"] = self["overall_ocr_res"].img["ocr_res_img"]

        if model_settings["use_table_recognition"] and len(self["table_res_list"]) > 0:
            table_cell_img = Image.fromarray(
                copy.deepcopy(self["doc_preprocessor_res"]["output_img"])
            )
            table_draw = ImageDraw.Draw(table_cell_img)
            rectangle_color = (255, 0, 0)
            for sno in range(len(self["table_res_list"])):
                table_res = self["table_res_list"][sno]
                cell_box_list = table_res["cell_box_list"]
                for box in cell_box_list:
                    x1, y1, x2, y2 = [int(pos) for pos in box]
                    table_draw.rectangle(
                        [x1, y1, x2, y2], outline=rectangle_color, width=2
                    )
            res_img_dict["table_cell_img"] = table_cell_img

        if model_settings["use_seal_recognition"] and len(self["seal_res_list"]) > 0:
            for sno in range(len(self["seal_res_list"])):
                seal_res = self["seal_res_list"][sno]
                seal_region_id = seal_res["seal_region_id"]
                sub_seal_res_dict = seal_res.img
                key = f"seal_res_region{seal_region_id}"
                res_img_dict[key] = sub_seal_res_dict["ocr_res_img"]

        # for layout ordering image
        image = Image.fromarray(self["doc_preprocessor_res"]["output_img"][:, :, ::-1])
        draw = ImageDraw.Draw(image, "RGBA")
        parsing_result = self["parsing_res_list"]
        for block in parsing_result:
            bbox = block["block_bbox"]
            index = block.get("index", None)
            label = block["sub_label"]
            fill_color = get_show_color(label)
            draw.rectangle(bbox, fill=fill_color)
            if index is not None:
                text_position = (bbox[2] + 2, bbox[1] - 10)
                draw.text(text_position, str(index), fill="red")

        res_img_dict["layout_order_res"] = image

        return res_img_dict

    def _to_str(self, *args, **kwargs) -> dict[str, str]:
        """Converts the instance's attributes to a dictionary and then to a string.

        Args:
            *args: Additional positional arguments passed to the base class method.
            **kwargs: Additional keyword arguments passed to the base class method.

        Returns:
            Dict[str, str]: A dictionary with the instance's attributes converted to strings.
        """
        data = {}
        data["input_path"] = self["input_path"]
        data["page_index"] = self["page_index"]
        model_settings = self["model_settings"]
        data["model_settings"] = model_settings
        if self["model_settings"]["use_doc_preprocessor"]:
            data["doc_preprocessor_res"] = self["doc_preprocessor_res"].str["res"]
        data["layout_det_res"] = self["layout_det_res"].str["res"]
        if model_settings["use_general_ocr"] or model_settings["use_table_recognition"]:
            data["overall_ocr_res"] = self["overall_ocr_res"].str["res"]
        if model_settings["use_table_recognition"] and len(self["table_res_list"]) > 0:
            data["table_res_list"] = []
            for sno in range(len(self["table_res_list"])):
                table_res = self["table_res_list"][sno]
                data["table_res_list"].append(table_res.str["res"])
        if model_settings["use_seal_recognition"] and len(self["seal_res_list"]) > 0:
            data["seal_res_list"] = []
            for sno in range(len(self["seal_res_list"])):
                seal_res = self["seal_res_list"][sno]
                data["seal_res_list"].append(seal_res.str["res"])
        if (
            model_settings["use_formula_recognition"]
            and len(self["formula_res_list"]) > 0
        ):
            data["formula_res_list"] = []
            for sno in range(len(self["formula_res_list"])):
                formula_res = self["formula_res_list"][sno]
                data["formula_res_list"].append(formula_res.str["res"])

        return JsonMixin._to_str(data, *args, **kwargs)

    def _to_json(self, *args, **kwargs) -> dict[str, str]:
        """
        Converts the object's data to a JSON dictionary.

        Args:
            *args: Positional arguments passed to the JsonMixin._to_json method.
            **kwargs: Keyword arguments passed to the JsonMixin._to_json method.

        Returns:
            Dict[str, str]: A dictionary containing the object's data in JSON format.
        """
        data = {}
        data["input_path"] = self["input_path"]
        data["page_index"] = self["page_index"]
        model_settings = self["model_settings"]
        data["model_settings"] = model_settings
        parsing_res_list = self["parsing_res_list"]
        parsing_res_list = [
            {
                "block_label": parsing_res["block_label"],
                "block_content": parsing_res["block_content"],
                "block_bbox": parsing_res["block_bbox"],
            }
            for parsing_res in parsing_res_list
        ]
        data["parsing_res_list"] = parsing_res_list
        if self["model_settings"]["use_doc_preprocessor"]:
            data["doc_preprocessor_res"] = self["doc_preprocessor_res"].json["res"]
        data["layout_det_res"] = self["layout_det_res"].json["res"]
        if model_settings["use_general_ocr"] or model_settings["use_table_recognition"]:
            data["overall_ocr_res"] = self["overall_ocr_res"].json["res"]
        if model_settings["use_table_recognition"] and len(self["table_res_list"]) > 0:
            data["table_res_list"] = []
            for sno in range(len(self["table_res_list"])):
                table_res = self["table_res_list"][sno]
                data["table_res_list"].append(table_res.json["res"])
        if model_settings["use_seal_recognition"] and len(self["seal_res_list"]) > 0:
            data["seal_res_list"] = []
            for sno in range(len(self["seal_res_list"])):
                seal_res = self["seal_res_list"][sno]
                data["seal_res_list"].append(seal_res.json["res"])
        if (
            model_settings["use_formula_recognition"]
            and len(self["formula_res_list"]) > 0
        ):
            data["formula_res_list"] = []
            for sno in range(len(self["formula_res_list"])):
                formula_res = self["formula_res_list"][sno]
                data["formula_res_list"].append(formula_res.json["res"])
        return JsonMixin._to_json(data, *args, **kwargs)

    def _to_html(self) -> dict[str, str]:
        """Converts the prediction to its corresponding HTML representation.

        Returns:
            Dict[str, str]: The str type HTML representation result.
        """
        model_settings = self["model_settings"]
        res_html_dict = {}
        if model_settings["use_table_recognition"] and len(self["table_res_list"]) > 0:
            for sno in range(len(self["table_res_list"])):
                table_res = self["table_res_list"][sno]
                table_region_id = table_res["table_region_id"]
                key = f"table_{table_region_id}"
                res_html_dict[key] = table_res.html["pred"]
        return res_html_dict

    def _to_xlsx(self) -> dict[str, str]:
        """Converts the prediction HTML to an XLSX file path.

        Returns:
            Dict[str, str]: The str type XLSX representation result.
        """
        model_settings = self["model_settings"]
        res_xlsx_dict = {}
        if model_settings["use_table_recognition"] and len(self["table_res_list"]) > 0:
            for sno in range(len(self["table_res_list"])):
                table_res = self["table_res_list"][sno]
                table_region_id = table_res["table_region_id"]
                key = f"table_{table_region_id}"
                res_xlsx_dict[key] = table_res.xlsx["pred"]
        return res_xlsx_dict

    def _to_markdown(self) -> dict:
        """
        Save the parsing result to a Markdown file.

        Returns:
            Dict
        """

        def _format_data(obj):

            def format_title(title):
                """
                Normalize chapter title.
                Add the '#' to indicate the level of the title.
                If numbering exists, ensure there's exactly one space between it and the title content.
                If numbering does not exist, return the original title unchanged.

                :param title: Original chapter title string.
                :return: Normalized chapter title string.
                """
                match = self.title_pattern.match(title)
                if match:
                    numbering = match.group(1).strip()
                    title_content = match.group(3).lstrip()
                    # Return numbering and title content separated by one space
                    title = numbering + " " + title_content

                title = title.rstrip(".")
                level = (
                    title.count(
                        ".",
                    )
                    + 1
                    if "." in title
                    else 1
                )
                return f"#{'#' * level} {title}".replace("-\n", "").replace(
                    "\n",
                    " ",
                )

            def format_centered_text(key):
                return (
                    f'<div style="text-align: center;">{block[key]}</div>'.replace(
                        "-\n",
                        "",
                    ).replace("\n", " ")
                    + "\n"
                )

            def format_image(label):
                img_tags = []
                image_path = "".join(block[label].keys())
                img_tags.append(
                    '<div style="text-align: center;"><img src="{}" alt="Image" /></div>'.format(
                        image_path.replace("-\n", "").replace("\n", " "),
                    ),
                )
                return "\n".join(img_tags)

            def format_first_line(templates, format_func, spliter):
                lines = block["block_content"].split(spliter)
                for idx in range(len(lines)):
                    line = lines[idx]
                    if line.strip() == "":
                        continue
                    if line.lower() in templates:
                        lines[idx] = format_func(line)
                    break
                return spliter.join(lines)

            def format_table():
                return "\n" + block["block_content"]

            def get_seg_flag(block, prev_block):

                seg_start_flag = True
                seg_end_flag = True

                block_box = block["block_bbox"]
                context_left_coordinate = block_box[0]
                context_right_coordinate = block_box[2]
                seg_start_coordinate = block.get("seg_start_coordinate")
                seg_end_coordinate = block.get("seg_end_coordinate")

                if prev_block is not None:
                    prev_block_bbox = prev_block["block_bbox"]
                    num_of_prev_lines = prev_block.get("num_of_lines")
                    pre_block_seg_end_coordinate = prev_block.get("seg_end_coordinate")

                    # update context_left_coordinate and context_right_coordinate
                    if context_left_coordinate < prev_block_bbox[2]:
                        context_left_coordinate = min(
                            prev_block_bbox[0], context_left_coordinate
                        )
                        context_right_coordinate = max(
                            prev_block_bbox[2], context_right_coordinate
                        )

                    # 判断是否需要分段
                    prev_end_space_small = (
                        prev_block_bbox[2] - pre_block_seg_end_coordinate < 10
                    )
                    current_start_space_small = (
                        seg_start_coordinate - context_left_coordinate < 10
                    )
                    overlap_blocks = context_left_coordinate < prev_block_bbox[2]
                    prev_lines_more_than_one = num_of_prev_lines > 1

                    if (
                        overlap_blocks
                        and current_start_space_small
                        and prev_lines_more_than_one
                    ) or (
                        prev_end_space_small
                        and current_start_space_small
                        and prev_lines_more_than_one
                    ):
                        seg_start_flag = False
                else:
                    if seg_start_coordinate - context_left_coordinate < 10:
                        seg_start_flag = False

                if context_right_coordinate - seg_end_coordinate < 10:
                    seg_end_flag = False

                return seg_start_flag, seg_end_flag

            handlers = {
                "paragraph_title": lambda: format_title(block["block_content"]),
                "doc_title": lambda: f"# {block['block_content']}".replace(
                    "-\n",
                    "",
                ).replace("\n", " "),
                "table_title": lambda: format_centered_text("block_content"),
                "figure_title": lambda: format_centered_text("block_content"),
                "chart_title": lambda: format_centered_text("block_content"),
                "text": lambda: block["block_content"]
                .replace("-\n", " ")
                .replace("\n", " "),
                "abstract": lambda: format_first_line(
                    ["摘要", "abstract"], lambda l: f"## {l}\n", " "
                ),
                "content": lambda: block["block_content"]
                .replace("-\n", "  \n")
                .replace("\n", "  \n"),
                "image": lambda: format_image("block_image"),
                "chart": lambda: format_image("block_image"),
                "formula": lambda: f"$${block['block_content']}$$",
                "table": format_table,
                "reference": lambda: format_first_line(
                    ["参考文献", "references"], lambda l: f"## {l}", "\n"
                ),
                "algorithm": lambda: block["block_content"].strip("\n"),
                "seal": lambda: f"Words of Seals:\n{block['block_content']}",
            }
            parsing_res_list = obj["parsing_res_list"]
            markdown_content = ""
            last_label = None
            seg_start_flag = None
            seg_end_flag = None
            prev_block = None
            page_first_element_seg_start_flag = None
            page_last_element_seg_end_flag = None
            parsing_res_list = sorted(
                parsing_res_list,
                key=lambda x: x.get("sub_index", 999),
            )
            for block in parsing_res_list:
                seg_start_flag, seg_end_flag = get_seg_flag(block, prev_block)

                label = block.get("block_label")
                page_first_element_seg_start_flag = (
                    seg_start_flag
                    if (page_first_element_seg_start_flag is None)
                    else page_first_element_seg_start_flag
                )
                handler = handlers.get(label)
                if handler:
                    prev_block = block
                    if label == last_label == "text" and seg_start_flag == False:
                        last_char_of_markdown = (
                            markdown_content[-1] if markdown_content else ""
                        )
                        first_char_of_handler = handler()[0] if handler() else ""
                        last_is_chinese_char = (
                            re.match(r"[\u4e00-\u9fff]", last_char_of_markdown)
                            if last_char_of_markdown
                            else False
                        )
                        first_is_chinese_char = (
                            re.match(r"[\u4e00-\u9fff]", first_char_of_handler)
                            if first_char_of_handler
                            else False
                        )
                        if not (last_is_chinese_char or first_is_chinese_char):
                            markdown_content += " " + handler()
                        else:
                            markdown_content += handler()
                    else:
                        markdown_content += (
                            "\n\n" + handler() if markdown_content else handler()
                        )
                    last_label = label
            page_last_element_seg_end_flag = seg_end_flag

            return markdown_content, (
                page_first_element_seg_start_flag,
                page_last_element_seg_end_flag,
            )

        markdown_info = dict()
        markdown_info["markdown_texts"], (
            page_first_element_seg_start_flag,
            page_last_element_seg_end_flag,
        ) = _format_data(self)
        markdown_info["page_continuation_flags"] = (
            page_first_element_seg_start_flag,
            page_last_element_seg_end_flag,
        )

        markdown_info["markdown_images"] = {}
        for img in self["imgs_in_doc"]:
            markdown_info["markdown_images"][img["path"]] = img["img"]

        return markdown_info
