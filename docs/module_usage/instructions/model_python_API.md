---
comments: true
---

# PaddleX单模型Python脚本使用说明

在使用Python脚本进行单模型快速推理前，请确保您已经按照[PaddleX本地安装教程](../../installation/installation.md)完成了PaddleX的安装。

## 一、使用示例

以图像分类模型为例，使用方式如下：

```python
from paddlex import create_model
model = create_model(model_name="PP-LCNet_x1_0")
output = model.predict("https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg", batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_img("./output/")
    res.save_to_json("./output/res.json")
```

简单来说，只需三步：

* 调用`create_model()`方法实例化预测模型对象；
* 调用预测模型对象的`predict()`方法进行推理预测；
* 调用`print()`、`save_to_xxx()`等相关方法对预测结果进行打印输出或是保存。

## 二、API说明

### 1. 调用`create_model()`方法实例化预测模型对象

* `create_model`：实例化预测模型对象；
  * 参数：
    * `model_name`：`str` 类型，模型名，如“PP-LCNet_x1_0”；
    * `model_dir`：`str` 类型，本地 inference 模型文件目录路径，如“/path/to/PP-LCNet_x1_0_infer/”，默认为 `None`，表示使用`model_name`指定的官方推理模型；
    * `batch_size`：`int` 类型，默认为 `1`；
    * `device`：`str` 类型，用于设置模型推理设备，如为GPU设置则可以指定卡号，如“cpu”、“gpu:2”，默认情况下，如有 GPU 设置则使用 0 号 GPU，否则使用 CPU；
    * `pp_option`：`PaddlePredictorOption` 类型，用于改变运行模式等配置项，关于推理配置的详细说明，请参考下文[4-推理配置](#4-推理配置)；
    * `use_hpip`：`bool` 类型，是否启用高性能推理插件；
    * `hpi_config`：`dict | None` 类型，高性能推理配置；
    * _`推理超参数`_：支持常见推理超参数的修改，具体参数说明详见具体模型文档；

### 2. 调用预测模型对象的`predict()`方法进行推理预测

* `predict`：使用定义的预测模型，对输入数据进行预测；
  * 参数：
    * `input`：任意类型，支持str类型表示的待预测数据文件路径，或是包含待预测文件的目录，或是网络URL；对于CV模型，支持numpy.ndarray表示的图像数据；对于TS模型，支持pandas.DataFrame类型数据；同样支持上述类型所构成的list类型；
  * 返回值：`generator`，需通过`for-in`或`next()`方式进行遍历，每次访问返回一个样本的预测结果；

### 3. 对预测结果进行可视化

模型的预测结果支持直接访问与保存等操作，可通过相应的属性或方法实现，具体如下：

#### 属性：

* `str`：`str` 类型表示的预测结果；
  * 返回值：`str` 类型，预测结果的str表示；
* `json`：json格式表示的预测结果；
  * 返回值：`dict` 类型；
* `img`：预测结果的可视化图，仅当该模型预测结果支持可视化表示时可用；
  * 返回值：`PIL.Image` 类型；
* `html`：预测结果的HTML表示，仅当该模型预测结果支持以HTML形式表示时可用；
  * 返回值：`str` 类型；
* _`更多`_：不同模型的预测结果支持不同的表示方式，更多属性请参考具体模型文档；

#### 方法：

* `print()`：将预测结果输出，需要注意，当预测结果不便于直接输出时，会省略相关内容；
  * 参数：
    * `json_format`：`bool`类型，默认为`False`，表示不使用json格式化输出；
    * `indent`：`int`类型，默认为`4`，当`json_format`为`True`时有效，表示json格式化的类型；
    * `ensure_ascii`：`bool`类型，默认为`False`，当`json_format`为`True`时有效；
  * 返回值：无；
* `save_to_json()`：将预测结果保存为json格式的文件，需要注意，当预测结果包含无法json序列化的数据时，会自动进行格式转换以实现序列化保存；
  * 参数：
    * `save_path`：`str`类型，结果保存的路径；
    * `indent`：`int`类型，默认为`4`，当`json_format`为`True`时有效，表示json格式化的类型；
    * `ensure_ascii`：`bool`类型，默认为`False`，当`json_format`为`True`时有效；
  * 返回值：无；
* `save_to_img()`：将预测结果可视化并保存为图像，仅当该模型预测结果支持以图像形式表示时可用；
  * 参数：
    * `save_path`：`str`类型，结果保存的路径；
  * 返回值：无；
* `save_to_csv()`：将预测结果保存为CSV文件，仅当该模型预测结果支持以CSV形式表示时可用；
  * 参数：
    * `save_path`：`str`类型，结果保存的路径；
  * 返回值：无；
* `save_to_html()`：将预测结果保存为HTML文件，仅当该模型预测结果支持以HTML形式表示时可用；
  * 参数：
    * `save_path`：`str`类型，结果保存的路径；
  * 返回值：无；
* `save_to_xlsx()`：将预测结果保存为XLSX文件，仅当该模型预测结果支持以XLSX形式表示时可用；
  * 参数：
    * `save_path`：`str`类型，结果保存的路径；
  * 返回值：无；
* _`更多`_：不同模型的预测结果支持不同的存储方式，更多方法请参考具体模型文档；

### 4. 推理配置

PaddleX 支持通过`PaddlePredictorOption`修改推理配置，相关API如下：

#### 属性：

* `device`：推理设备；
  * 支持设置 `str` 类型表示的推理设备类型及卡号，设备类型支持可选 “gpu”、“cpu”、“npu”、“xpu”、“mlu”、“dcu”，当使用加速卡时，支持指定卡号，如使用 0 号 GPU：`gpu:0`，默认情况下，如有 GPU 设置则使用 0 号 GPU，否则使用 CPU；
  * 返回值：`str`类型，当前设置的推理设备。
* `run_mode`：运行模式；
  * 支持设置 `str` 类型的运行模式，支持可选 'paddle'，'trt_fp32'，'trt_fp16'，'trt_int8'，'mkldnn'，'mkldnn_bf16'，其中 'trt_fp32' 和' trt_fp16' 分别对应使用 TensorRT 子图引擎进行 FP32 和 FP16 精度的推理，仅当推理设备使用 GPU 时可选，'mkldnn' 仅当推理设备使用 CPU 时可选，默认为 'paddle'；
  * 返回值：`str`类型，当前设置的运行模式。
* `cpu_threads`：cpu 加速库计算线程数，仅当推理设备使用 cpu 时有效；
  * 支持设置 `int` 类型，cpu 推理时加速库计算线程数；
  * 返回值：`int` 类型，当前设置的加速库计算线程数。
* `trt_dynamic_shapes`：TensorRT 动态形状配置，仅当 `run_mode` 为 'trt_fp32' 或 'trt_fp16' 时有效；
  * 支持设置：`dict` 类型或 `None`，如果为 `dict`，键为输入张量名称，值为一个两级嵌套列表：`[{最小形状}, {优化形状}, {最大形状}]`，例如 `[[1, 2], [1, 2], [2, 2]]`；
  * 返回值：`dict` 类型或 `None`，当前设置的 TensorRT 动态形状配置。
* `trt_dynamic_shape_input_data`：使用 TensorRT 时，为用于构建引擎的输入张量填充的数据，仅当 `run_mode` 为 'trt_fp32' 或 'trt_fp16' 时有效；
  * 支持设置：`dict` 类型或 `None`，如果为 `dict`，键为输入张量名称，值为一个两级嵌套列表：`[{最小形状对应的填充数据}, {优化形状对应的填充数据}, {最大形状对应的填充数据}]`，例如 `[[1.0, 1.0], [1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]`，数据为浮点数，按照行优先顺序填充；
  * 返回值：`dict` 类型或 `None`，当前设置的输入张量填充数据。

#### 方法：

* `get_support_run_mode`：获取支持的运行模式；
  * 参数：无；
  * 返回值：list 类型，可选的运行模式。
* `get_support_device`：获取支持的运行设备类型；
  * 参数：无；
  * 返回值：list 类型，可选的设备类型。
* `get_device`：获取当前设置的设备；
  * 参数：无；
  * 返回值：str 类型。
