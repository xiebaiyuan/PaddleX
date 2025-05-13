---
comments: true
---

# PaddleX 高性能推理指南

在实际生产环境中，许多应用对部署策略的性能指标（尤其是响应速度）有着较严苛的标准，以确保系统的高效运行与用户体验的流畅性。为此，PaddleX 提供高性能推理插件，通过自动配置和多后端推理功能，让用户无需关注复杂的配置和底层细节，即可显著提升模型的推理速度。除了支持产线的推理加速外，PaddleX 高性能推理插件也可用于单独使用模块时的推理加速。

## 目录

- [1. 安装与基础使用方法](#1.-安装与基础使用方法)
  - [1.1 安装高性能推理插件](#1.1-安装高性能推理插件)
  - [1.2 启用高性能推理插件](#1.2-启用高性能推理插件)
- [2. 进阶使用方法](#2-进阶使用方法)
  - [2.1 高性能推理工作模式](#21-高性能推理工作模式)
  - [2.2 高性能推理配置](#22-高性能推理配置)
  - [2.3 修改高性能推理配置](#23-修改高性能推理配置)
  - [2.4 在配置文件中启用/禁用高性能推理插件](#24-在配置文件中启用禁用高性能推理插件)
  - [2.5 模型缓存说明](#25-模型缓存说明)
  - [2.6 定制模型推理库](#26-定制模型推理库)
- [3. 常见问题](#3.-常见问题)

## 1. 安装与基础使用方法

使用高性能推理插件前，请确保您已经按照 [PaddleX本地安装教程](../installation/installation.md) 完成了 PaddleX 的安装，且按照 PaddleX 产线命令行使用说明或 PaddleX 产线 Python 脚本使用说明跑通了产线的快速推理。

高性能推理插件支持处理 **飞桨静态图（`.pdmodel`、 `.json`）**、**ONNX（`.onnx`）**、**华为 OM（`.om`）** 等多种模型格式。对于 ONNX 模型，可以使用 [Paddle2ONNX 插件](./paddle2onnx.md) 转换得到。如果模型目录中存在多种格式的模型，PaddleX 会根据需要自动选择，并可能进行自动模型转换。

### 1.1 安装高性能推理插件

目前高性能推理支持的处理器架构、操作系统、设备类型和 Python 版本如下表所示：

<table>
  <tr>
    <th>操作系统</th>
    <th>处理器架构</th>
    <th>设备类型</th>
    <th>Python 版本</th>
  </tr>
  <tr>
    <td rowspan="5">Linux</td>
    <td rowspan="4">x86-64</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>3.8–3.12</td>
  </tr>
  <tr>
    <td>GPU&nbsp;（CUDA&nbsp;11.8&nbsp;+&nbsp;cuDNN&nbsp;8.9）</td>
    <td>3.8–3.12</td>
  </tr>
  <tr>
    <td>NPU</td>
    <td>3.10</td>
  </tr>
  <tr>
    <td>AArch64</td>
    <td>NPU</td>
    <td>3.10</td>
  </tr>
</table>

#### 1.1.1 在 Docker 容器中安装高性能推理插件（强烈推荐）

参考 [基于Docker获取PaddleX](../installation/installation.md#21-基于docker获取paddlex) 使用 Docker 启动 PaddleX 容器。启动容器后，根据设备类型，执行如下指令，安装高性能推理插件：

  <table>
      <thead>
          <tr>
              <th>设备类型</th>
              <th>安装指令</th>
              <th>说明</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>CPU</td>
              <td><code>paddlex --install hpi-cpu</code></td>
              <td>安装 CPU 版本的高性能推理功能。</td>
          </tr>
          <tr>
              <td>GPU</td>
              <td><code>paddlex --install hpi-gpu</code></td>
              <td>安装 GPU 版本的高性能推理功能。<br />包含了 CPU 版本的所有功能。</td>
          </tr>
      </tbody>
  </table>

PaddleX 官方 Docker 镜像中预装了 Paddle2ONNX 插件，以便 PaddleX 可以在需要时转换模型格式。此外，GPU 版本的镜像中安装了 TensorRT，高性能推理插件可以使用 Paddle Inference TensorRT 子图引擎进行推理加速。

**请注意，以上提到的镜像指的是 [基于Docker获取PaddleX](../installation/installation.md#21-基于docker获取paddlex) 中描述的 PaddleX 官方镜像，而非 [飞桨PaddlePaddle本地安装教程](../installation/paddlepaddle_install.md#基于-docker-安装飞桨) 中描述的飞桨框架官方镜像。对于后者，请参考高性能推理插件本地安装说明。**

#### 1.1.2 本地安装高性能推理插件

**建议在安装高性能推理插件前，首先安装 Paddle2ONNX 插件，以便 PaddleX 可以在需要时转换模型格式。**

**安装 CPU 版本的高性能推理插件：**

执行：

```bash
paddlex --install hpi-cpu
```

**安装 GPU 版本的高性能推理插件：**

在安装前，需要确保环境中安装有 CUDA 与 cuDNN。目前 PaddleX 官方仅提供 CUDA 11.8 + cuDNN 8.9 的预编译包，请保证安装的 CUDA 和 cuDNN 版本与编译版本兼容。以下分别是 CUDA 11.8 和 cuDNN 8.9 的安装说明文档：

- [安装 CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
- [安装 cuDNN 8.9](https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html)

如果使用的是飞桨框架官方镜像，则镜像中的 CUDA 和 cuDNN 版本已经是满足要求的，无需额外安装。

如果通过 pip 安装飞桨，通常 CUDA、cuDNN 的相关 Python 包将被自动安装。在这种情况下，**仍需要通过安装非 Python 专用的 CUDA 与 cuDNN**。同时，建议安装的 CUDA 和 cuDNN 版本与环境中存在的 Python 包版本保持一致，以避免不同版本的库共存导致的潜在问题。可以通过如下方式可以查看 CUDA 和 cuDNN 相关 Python 包的版本：

```bash
# CUDA 相关 Python 包版本
pip list | grep nvidia-cuda
# cuDNN 相关 Python 包版本
pip list | grep nvidia-cudnn
```

如果希望使用 Paddle Inference TensorRT 子图引擎，需额外安装 TensorRT。请参考 [飞桨PaddlePaddle本地安装教程](../installation/paddlepaddle_install.md) 中的相关说明。需要注意的是，由于高性能推理插件的底层推理库也集成了 TensorRT，建议安装相同版本的 TensorRT 以避免版本冲突。目前，高性能推理插件的底层推理库集成的 TensorRT 版本为 8.6.1.6。如果使用的是飞桨框架官方镜像，则无需关心版本冲突问题。

确认安装了正确版本的 CUDA、cuDNN、以及 TensorRT （可选）后，执行：

```bash
paddlex --install hpi-gpu
```

**安装 NPU 版本的高性能推理插件：**

请参考 [昇腾 NPU 高性能推理教程](../practical_tutorials/high_performance_npu_tutorial.md)。

**注意：**

1. **目前 PaddleX 官方仅提供 CUDA 11.8 + cuDNN 8.9 的预编译包**。CUDA 12 已经在支持中。

2. 同一环境中只应该存在一个版本的高性能推理插件。

3. 对于 Windows 系统，目前建议在 Docker 容器或者 [WSL](https://learn.microsoft.com/zh-cn/windows/wsl/install) 环境中安装和使用高性能推理插件。

### 1.2 启用高性能推理插件

以下是使用 PaddleX CLI 和 Python API 在通用图像分类产线和图像分类模块中启用高性能推理插件的示例。

对于 PaddleX CLI，指定 `--use_hpip`，即可启用高性能推理插件。

通用图像分类产线：

```bash
paddlex \
    --pipeline image_classification \
    --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg \
    --use_hpip
```

图像分类模块：

```bash
python main.py \
    -c paddlex/configs/modules/image_classification/ResNet18.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir=None \
    -o Predict.input=https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg \
    -o Predict.use_hpip=True
```

对于 PaddleX Python API，启用高性能推理插件的方法类似。以通用图像分类产线和图像分类模块为例：

通用图像分类产线：

```python
from paddlex import create_pipeline

pipeline = create_pipeline(
    pipeline="image_classification",
    use_hpip=True
)

output = pipeline.predict("https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg")
```

图像分类模块：

```python
from paddlex import create_model

model = create_model(
    model_name="ResNet18",
    use_hpip=True
)

output = model.predict("https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg")
```

启用高性能推理插件得到的推理结果与未启用插件时一致。对于部分模型，**在首次启用高性能推理插件时，可能需要花费较长时间完成推理引擎的构建**。PaddleX 将在推理引擎的第一次构建完成后将相关信息缓存在模型目录，并在后续复用缓存中的内容以提升初始化速度。

**通过 PaddleX CLI 和 Python API 启用高性能推理插件默认作用于整条产线/模块**，若想细粒度控制作用范围，如只对产线中某条子产线或某个子模块启用高性能推理插件，可以在产线配置文件中不同层级的配置里设置 `use_hpip`，请参考 [2.4 在配置文件中启用/禁用高性能推理插件](#24-在配置文件中启用禁用高性能推理插件)。如果 CLI 参数、API 参数以及配置文件中均未指定 `use_hpip`，默认不启用高性能推理插件。

## 2. 进阶使用方法

本节介绍高性能推理插件的进阶使用方法，适合对模型部署有一定了解或希望进行手动配置调优的用户。用户可以参照配置说明和示例，根据自身需求自定义使用高性能推理插件。接下来将对高性能推理插件进阶使用方法进行详细介绍。

### 2.1 高性能推理工作模式

高性能推理插件支持两种工作模式。通过修改高性能推理配置，可以切换不同的工作模式。

#### 2.1.1 安全自动配置模式

安全自动配置模式，具有保护机制，默认**自动选用当前环境性能较优的配置**。在这种模式下，用户可以覆盖默认配置，但用户提供的配置将受到检查，PaddleX将根据先验知识拒绝不可用的配置。这是默认的工作模式。

#### 2.1.2 无限制手动配置模式

无限制手动配置模式，提供完全的配置自由，可以**自由选择推理后端、修改后端配置等**，但无法保证推理一定成功。此模式适合有经验和对推理后端及其配置有明确需求的用户，建议在熟悉高性能推理的情况下使用。

### 2.2 高性能推理配置

常用高性能推理配置项包括：

<table>
<thead>
<tr>
<th>名称</th>
<th>说明</th>
<th>类型</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>auto_config</code></td>
<td>是否启用安全自动配置模式。<br /><code>True</code> 为启用安全自动配置模式，<code>False</code> 为启用无限制手动配置模式。</td>
<td><code>bool</code></td>
<td><code>True</code></td>
</tr>
<tr>
  <td><code>backend</code></td>
  <td>用于指定要使用的推理后端。在无限制手动配置模式下不能为 <code>None</code>。</td>
  <td><code>str | None</code></td>
  <td><code>None</code></td>
</tr>
<tr>
  <td><code>backend_config</code></td>
  <td>推理后端的配置，若不为 <code>None</code> 则可以覆盖推理后端的默认配置项。</td>
  <td><code>dict | None</code></td>
  <td><code>None</code></td>
</tr>
<tr>
  <td><code>auto_paddle2onnx</code></td>
  <td>是否将飞桨静态图模型自动转换为 ONNX 模型。当 Paddle2ONNX 插件不可用时，不执行转换。</td>
  <td><code>bool</code></td>
  <td><code>True</code></td>
</tr>
</tbody>
</table>

`backend` 可选值如下表所示：

<table>
  <tr>
    <th>选项</th>
    <th>描述</th>
    <th>支持设备</th>
  </tr>
  <tr>
    <td><code>paddle</code></td>
    <td>Paddle Inference 推理引擎，支持通过 Paddle Inference TensorRT 子图引擎的方式提升模型的 GPU 推理性能。</td>
    <td>CPU，GPU，NPU</td>
  </tr>
  <tr>
    <td><code>openvino</code></td>
    <td><a href="https://github.com/openvinotoolkit/openvino">OpenVINO</a>，Intel 提供的深度学习推理工具，优化了多种 Intel 硬件上的模型推理性能。</td>
    <td>CPU</td>
  </tr>
  <tr>
    <td><code>onnxruntime</code></td>
    <td><a href="https://onnxruntime.ai/">ONNX Runtime</a>，跨平台、高性能的推理引擎。</td>
    <td>CPU，GPU</td>
  </tr>
  <tr>
    <td><code>tensorrt</code></td>
    <td><a href="https://developer.nvidia.com/tensorrt">TensorRT</a>，NVIDIA 提供的高性能深度学习推理库，针对 NVIDIA GPU 进行优化以提升速度。</td>
    <td>GPU</td>
  </tr>
  <tr>
    <td><code>om</code></td>
    <td>华为昇腾 NPU 定制的离线模型格式对应的推理引擎，针对硬件进行了深度优化，减少算子计算时间和调度时间，能够有效提升推理性能。</td>
    <td>NPU</td>
  </tr>
</table>

`backend_config` 对不同的后端有不同的配置项，如下表所示：

<table>
  <tr>
    <th>后端</th>
    <th>配置项</th>
  </tr>
  <tr>
    <td><code>paddle</code></td>
    <td>参考 <a href="../module_usage/instructions/model_python_API.md#4-推理配置">PaddleX单模型Python脚本使用说明</a>。可通过键值对配置 <code>PaddlePredictorOption</code> 对象的属性，例如 <code>run_mode</code>。</td>
  </tr>
  <tr>
    <td><code>openvino</code></td>
    <td><code>cpu_num_threads</code>（<code>int</code>）：CPU 推理使用的逻辑处理器数量。默认为 <code>8</code>。</td>
  </tr>
  <tr>
    <td><code>onnxruntime</code></td>
    <td><code>cpu_num_threads</code>（<code>int</code>）：CPU 推理时算子内部的并行计算线程数。默认为 <code>8</code>。</td>
  </tr>
  <tr>
    <td><code>tensorrt</code></td>
    <td>
      <code>precision</code>（<code>str</code>）：使用的精度，<code>"fp16"</code> 或 <code>"fp32"</code>。默认为 <code>"fp32"</code>。
      <br />
      <code>dynamic_shapes</code>（<code>dict</code>）：动态形状配置，指定每个输入对应的最小形状、优化形状以及最大形状。格式为：<code>{输入张量名称}: [{最小形状}, {优化形状}, {最大形状}]</code>。动态形状是 TensorRT 延迟指定部分或全部张量维度直到运行时的能力，更多介绍请参考 <a href="https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/work-dynamic-shapes.html">TensorRT 官方文档</a>。
    </td>
  </tr>
  <tr>
    <td><code>om</code></td>
    <td>暂无</td>
  </tr>
</table>

### 2.3 修改高性能推理配置

模型初始化时，日志中默认会记录将要使用的高性能推理配置。由于实际部署环境和需求的多样性，默认配置可能无法满足所有要求。这时，可能需要手动调整高性能推理配置。用户可以通过修改产线/模块配置文件、CLI或Python API所传递参数中的 `hpi_config` 字段内容来修改配置。通过 CLI 或 Python API 传递的参数将覆盖产线/模块配置文件中的设置。配置文件中不同层级的配置将自动合并，最深层的配置具有最高的优先级。以下将结合一些例子介绍如何修改配置。

**通用OCR产线的所有模型使用 `onnxruntime` 后端：**

<details><summary>👉 修改产线配置文件方式（点击展开）</summary>

```yaml
...
hpi_config:
  backend: onnxruntime
```

</details>
<details><summary>👉 CLI 传参方式（点击展开）</summary>

```bash
paddlex \
    --pipeline image_classification \
    --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg \
    --use_hpip \
    --hpi_config '{"backend": "onnxruntime"}'
```

</details>
<details><summary>👉 Python API 传参方式（点击展开）</summary>

```python
from paddlex import create_pipeline

pipeline = create_pipeline(
    pipeline="OCR",
    use_hpip=True,
    hpi_config={"backend": "onnxruntime"}
)
```

</details>

**图像分类模块使用 `onnxruntime` 后端：**

<details><summary>👉 修改产线配置文件方式（点击展开）</summary>

```yaml
Predict:
  ...
  hpi_config:
    backend: onnxruntime
```

</details>
<details><summary>👉 CLI 传参方式（点击展开）</summary>

```bash
python main.py \
    -c paddlex/configs/modules/image_classification/ResNet18.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir=None \
    -o Predict.input=https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg \
    -o Predict.use_hpip=True \
    -o Predict.hpi_config='{"backend": "onnxruntime"}'
```

</details>
<details><summary>👉 Python API 传参方式（点击展开）</summary>

```python
from paddlex import create_model

model = create_model(
    model_name="ResNet18",
    use_hpip=True,
    hpi_config={"backend": "onnxruntime"}
)
```

</details>

**通用OCR产线的 `text_detection` 模块使用 `onnxruntime` 后端，`text_recognition` 模块使用 `tensorrt` 后端：**

<details><summary>👉 修改产线配置文件方式（点击展开）</summary>

```yaml
SubModules:
  TextDetection:
    ...
    hpi_config:
      backend: onnxruntime
  TextRecognition:
    ...
    hpi_config:
      backend: tensorrt
```

</details>

**通用图像分类产线修改动态形状配置：**

<details><summary>👉 修改产线配置文件方式（点击展开）</summary>

```yaml
  SubModules:
    ImageClassification:
      hpi_config:
        ...
        backend: tensorrt
        backend_config:
          dynamic_shapes:
            x:
              - [1, 3, 300, 300]
              - [4, 3, 300, 300]
              - [32, 3, 1200, 1200]
```

</details>

**图像分类模块修改 TensorRT 动态形状配置：**

<details><summary>👉 修改产线配置文件方式（点击展开）</summary>

```yaml
Predict:
  hpi_config:
    ...
    backend: tensorrt
    backend_config:
      dynamic_shapes:
        x:
          - [1, 3, 300, 300]
          - [4, 3, 300, 300]
          - [32, 3, 1200, 1200]
```

</details>

### 2.4 在配置文件中启用/禁用高性能推理插件

在配置文件中，可以使用 `use_hpip` 控制高性能推理插件的启用和禁用。与通过 CLI 和 API 配置不同的是，这种方式支持通过在子产线/子模块级别使用 `use_hpip`，实现**仅产线中的某个子产线/子模块使用高性能推理**。示例如下：

**通用OCR产线的 `text_detection` 模块使用高性能推理，`text_recognition` 模块不使用高性能推理：**

<details><summary>👉 点击展开</summary>

```yaml
SubModules:
  TextDetection:
    ...
    use_hpip: True # 当前子模块使用高性能推理
  TextLineOrientation:
    ...
    # 当前子模块未单独配置，默认与全局配置一致（如果配置文件和 CLI、API 参数均未设置，则不使用高性能推理）
  TextRecognition:
    ...
    use_hpip: False # 当前子模块不使用高性能推理
```

</details>

**注意：**

1. 在配置文件中的多个层级设置 `use_hpip` 时，将以最深层的配置为准。
2. **当通过修改产线配置文件的方式启用/禁用高性能推理插件时，不建议同时使用 CLI 或 Python API 的方式进行设置。** 通过 CLI 或 Python API 设置 `use_hpip` 等同于修改配置文件顶层的 `use_hpip`。

### 2.5 模型缓存说明

模型缓存会存放在模型目录下的 `.cache` 目录中。

**修改 Paddle Inference TensorRT 子图引擎或 TensorRT 相关配置后，建议清理缓存，以避免出现缓存导致新配置不生效的情况。**

当启用`auto_paddle2onnx`选项时，可能会在模型目录下自动生成`inference.onnx`文件。

### 2.6 定制模型推理库

`ultra-infer` 是高性能推理底层依赖的模型推理库，在 `PaddleX/libs/ultra-infer` 目录以子项目形式维护。PaddleX 提供 `ultra-infer` 的构建脚本，位于 `PaddleX/libs/ultra-infer/scripts/linux/set_up_docker_and_build_py.sh` 。编译脚本默认构建 GPU 版本的 `ultra-infer`，集成 OpenVINO、TensorRT、ONNX Runtime 三种推理后端。

如果需要自定义构建 `ultra-infer`，可根据需求修改构建脚本的如下选项：

<table>
    <thead>
        <tr>
            <th>选项</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>http_proxy</td>
            <td>在下载三方库时使用的 HTTP 代理，默认为空</td>
        </tr>
        <tr>
            <td>PYTHON_VERSION</td>
            <td>Python 版本，默认 <code>3.10.0</code></td>
        </tr>
        <tr>
            <td>WITH_GPU</td>
            <td>是否支持 GPU，默认 <code>ON</code></td>
        </tr>
        <tr>
            <td>ENABLE_ORT_BACKEND</td>
            <td>是否集成 ONNX Runtime 后端，默认 <code>ON</code></td>
        </tr>
        <tr>
            <td>ENABLE_TRT_BACKEND</td>
            <td>是否集成 TensorRT 后端（仅支持GPU），默认 <code>ON</code></td>
        </tr>
        <tr>
            <td>ENABLE_OPENVINO_BACKEND</td>
            <td>是否集成 OpenVINO 后端（仅支持CPU），默认 <code>ON</code></td>
        </tr>
    </tbody>
</table>

示例：

```bash
# 构建
cd PaddleX/libs/ultra-infer/scripts/linux
# export PYTHON_VERSION=...
# export WITH_GPU=...
# export ENABLE_ORT_BACKEND=...
# export ...
bash set_up_docker_and_build_py.sh

# 安装
python -m pip install ../../python/dist/ultra_infer*.whl
```

## 3. 常见问题

**1. 为什么开启高性能推理插件前后，感觉推理速度没有明显提升？**

高性能推理插件通过智能选择和配置后端来实现推理加速。由于模型结构复杂或存在不支持算子等情况，部分模型可能无法实现加速。此时，PaddleX 会在日志中给出相应提示。可以使用 [PaddleX benchmark 功能](../module_usage/instructions/benchmark.md) 测量模块中各部分的推理耗时情况，以便更准确地评估性能。此外，对于产线而言，推理的性能瓶颈可能不在模型推理上，而在串联逻辑上，这也可能导致加速效果不明显。

**2. 是否所有产线与模块均支持高性能推理？**

所有使用静态图模型的产线与模块都支持启用高性能推理插件，但部分模型在某些情况下可能无法获得推理加速，具体原因可以参考问题1。

**3. 为什么安装高性能推理插件会失败，日志显示：“You are not using PaddlePaddle compiled with CUDA 11. Currently, CUDA versions other than 11.x are not supported by the high-performance inference plugin.”？**

对于 GPU 版本的高性能推理插件，目前 PaddleX 官方仅提供 CUDA 11.8 + cuDNN 8.9 的预编译包。CUDA 12 目前正在支持中。

**4. 为什么使用高性能推理功能后，程序在运行过程中会卡住或者显示一些“WARNING”和“ERROR”信息？这种情况下应该如何处理？**

在初始化模型时，子图优化等操作可能会导致程序耗时较长，并生成一些“WARNING”和“ERROR”信息。然而，只要程序没有自动退出，建议耐心等待，程序通常会继续运行至完成。

**5. 使用 GPU 推理时，启用高性能推理插件后显存占用增大并导致 OOM，如何解决？**

部分提速手段会以牺牲显存为代价，以支持更广泛的推理场景。如果显存成为瓶颈，可参考以下优化思路：

- 调整产线配置：禁用不需要使用的功能，避免加载多余模型；根据业务需求合理降低 batch size，平衡吞吐与显存使用。
- 切换推理后端：不同推理后端在显存管理策略上各有差异，可尝试各种后端测评显存占用与性能。
- 优化动态形状配置：对于使用 TensorRT 或 Paddle Inference TensorRT 子图引擎的模块，根据实际输入数据的分布，缩小动态形状范围。
