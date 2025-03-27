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


import os
import glob
import itertools
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def readme():
    """get readme"""
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()


def dependencies():
    """get dependencies"""
    with open("requirements.txt", "r") as file:
        return file.read()


def serving_dependencies():
    with open(os.path.join("paddlex", "serving_requirements.txt"), "r") as file:
        return file.read()


def paddle2onnx_dependencies():
    with open(os.path.join("paddlex", "paddle2onnx_requirements.txt"), "r") as file:
        return file.read()


def version():
    """get version"""
    with open(os.path.join("paddlex", ".version"), "r") as file:
        return file.read().rstrip()


def get_data_files(directory: str, filetypes: list = None):
    all_files = []
    filetypes = filetypes or []

    for root, _, files in os.walk(directory):
        rel_root = os.path.relpath(root, directory)
        for file in files:
            filepath = os.path.join(rel_root, file)
            filetype = os.path.splitext(file)[1][1:]
            if filetype in filetypes:
                all_files.append(filepath)

    return all_files


def packages_and_package_data():
    """get packages and package_data"""

    def _recursively_find(pattern, exts=None):
        for dir_ in glob.iglob(pattern):
            for root, _, files in os.walk(dir_):
                for f in files:
                    if exts is not None:
                        ext = os.path.splitext(f)[1]
                        if ext not in exts:
                            continue
                    yield os.path.join(root, f)

    pkgs = find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"])
    pkg_data = []
    for p in itertools.chain(
        _recursively_find("paddlex/configs/*", exts=[".yml", ".yaml"]),
    ):
        if Path(p).suffix in (".pyc", ".pyo"):
            continue
        pkg_data.append(Path(p).relative_to("paddlex").as_posix())
    pipeline_config = [
        Path(p).relative_to("paddlex").as_posix()
        for p in glob.glob("paddlex/pipelines/*.yaml")
    ]
    pkg_data.append("inference/pipelines/ppchatocrv3/ch_prompt.yaml")
    pkg_data.extend(pipeline_config)
    pkg_data.append(".version")
    pkg_data.append("repo_manager/requirements.txt")
    pkg_data.append("serving_requirements.txt")
    pkg_data.append("paddle2onnx_requirements.txt")
    pkg_data.append("hpip_links.html")
    pkg_data.append("inference/utils/hpi_model_info_collection.json")
    ops_file_dir = "paddlex/ops"
    ops_file_types = ["h", "hpp", "cpp", "cc", "cu"]
    return pkgs, {
        "paddlex.ops": get_data_files(ops_file_dir, ops_file_types),
        "paddlex": pkg_data,
    }


if __name__ == "__main__":
    pkgs, pkg_data = packages_and_package_data()

    s = setup(
        name="paddlex",
        version=version(),
        description=("Low-code development tool based on PaddlePaddle."),
        long_description=readme(),
        long_description_content_type="text/markdown",
        author="PaddlePaddle Authors",
        author_email="",
        install_requires=dependencies(),
        extras_require={
            "serving": serving_dependencies(),
            "paddle2onnx": paddle2onnx_dependencies(),
        },
        packages=pkgs,
        package_data=pkg_data,
        entry_points={
            "console_scripts": [
                "paddlex = paddlex.__main__:console_entry",
            ],
        },
        # PyPI package information
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        license="Apache 2.0",
        keywords=["paddlepaddle"],
    )
