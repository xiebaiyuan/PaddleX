---
comments: true
---

# 文本检测模块使用教程

## 一、概述
文本检测模块是OCR（光学字符识别）系统中的关键组成部分，负责在图像中定位和标记出包含文本的区域。该模块的性能直接影响到整个OCR系统的准确性和效率。文本检测模块通常会输出文本区域的边界框（Bounding Boxes），这些边界框将作为输入传递给文本识别模块进行后续处理。

## 二、支持模型列表


<table>
<thead>
<tr>
<th>模型</th><th>模型下载链接</th>
<th>检测Hmean（%）</th>
<th>GPU推理耗时（ms）<br/>[常规模式 / 高性能模式]</th>
<th>CPU推理耗时（ms）<br/>[常规模式 / 高性能模式]</th>
<th>模型存储大小（M)</th>
<th>介绍</th>
</tr>
</thead>
<tbody>
<tr>
<td>PP-OCRv4_server_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_server_det_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_server_det_pretrained.pdparams">训练模型</a></td>
<td>82.56</td>
<td>83.34 / 80.91</td>
<td>442.58 / 442.58</td>
<td>109</td>
<td>PP-OCRv4 的服务端文本检测模型，精度更高，适合在性能较好的服务器上部署</td>
</tr>
<tr>
<td>PP-OCRv4_mobile_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_mobile_det_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_mobile_det_pretrained.pdparams">训练模型</a></td>
<td>77.35</td>
<td>8.79 / 3.13</td>
<td>51.00 / 28.58</td>
<td>4.7</td>
<td>PP-OCRv4 的移动端文本检测模型，效率更高，适合在端侧设备部署</td>
</tr>
<tr>
<td>PP-OCRv3_mobile_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv3_mobile_det_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv3_mobile_det_pretrained.pdparams">训练模型</a></td>
<td>78.68</td>
<td>8.44 / 2.91</td>
<td>27.87 / 27.87</td>
<td>2.1</td>
<td>PP-OCRv3 的移动端文本检测模型，效率更高，适合在端侧设备部署</td>
</tr>
<tr>
<td>PP-OCRv3_server_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv3_server_det_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv3_server_det_pretrained.pdparams">训练模型</a></td>
<td>80.11</td>
<td>65.41 / 13.67</td>
<td>305.07 / 305.07</td>
<td>102.1</td>
<td>PP-OCRv3 的服务端文本检测模型，精度更高，适合在性能较好的服务器上部署</td>
</tr>
</tbody>
</table>

<strong>测试环境说明:</strong>

  <ul>
      <li><b>性能测试环境</b>
          <ul>
              <li><strong>测试数据集：</strong>PaddleOCR 自建的中英文数据集，覆盖街景、网图、文档、手写多个场景，其中文本检测包含 593 张图片。</li>
              <li><strong>硬件配置：</strong>
                  <ul>
                      <li>GPU：NVIDIA Tesla T4</li>
                      <li>CPU：Intel Xeon Gold 6271C @ 2.60GHz</li>
                      <li>其他环境：Ubuntu 20.04 / cuDNN 8.6 / TensorRT 8.5.2.2</li>
                  </ul>
              </li>
          </ul>
      </li>
      <li><b>推理模式说明</b></li>
  </ul>

<table border="1">
    <thead>
        <tr>
            <th>模式</th>
            <th>GPU配置</th>
            <th>CPU配置</th>
            <th>加速技术组合</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>常规模式</td>
            <td>FP32精度 / 无TRT加速</td>
            <td>FP32精度 / 8线程</td>
            <td>PaddleInference</td>
        </tr>
        <tr>
            <td>高性能模式</td>
            <td>选择先验精度类型和加速策略的最优组合</td>
            <td>FP32精度 / 8线程</td>
            <td>选择先验最优后端（Paddle/OpenVINO/TRT等）</td>
        </tr>
    </tbody>
</table>

## 三、快速集成
> ❗ 在快速集成前，请先安装 PaddleX 的 wheel 包，详细请参考 [PaddleX本地安装教程](../../../installation/installation.md)。
>
几行代码即可完成文本检测模块的推理，可以任意切换该模块下的模型，您也可以将文本检测的模块中的模型推理集成到您的项目中。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_001.png)到本地。

```python
from paddlex import create_model
model = create_model(model_name="PP-OCRv4_mobile_det")
output = model.predict("general_ocr_001.png", batch_size=1)
for res in output:
    res.print()
    res.save_to_img(save_path="./output/")
    res.save_to_json(save_path="./output/res.json")
```

运行后，得到的结果为：

```bash
{'res': {'input_path': 'general_ocr_001.png', "page_index": None, 'dt_polys': [[[73, 552], [453, 542], [454, 575], [74, 585]], [[17, 506], [515, 486], [517, 535], [19, 555]], [[189, 457], [398, 449], [399, 482], [190, 490]], [[41, 412], [484, 387], [486, 433], [43, 457]]], 'dt_scores': [0.7555687038101032, 0.701620896397861, 0.8839516283528792, 0.8123399529333318]}}
```

运行结果参数含义如下：
- `input_path`：表示输入待预测图像的路径
- `page_index`：如果输入是PDF文件，则表示当前是PDF的第几页，否则为 `None`
- `dt_polys`：表示预测的文本检测框，其中每个文本检测框包含一个四边形的四个顶点。其中每个顶点都是一个列表，分别表示该顶点的x坐标和y坐标
- `dt_scores`：表示预测的文本检测框的置信度

可视化图片如下：

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/modules/text_det/general_ocr_001_res.png"/>

相关方法、参数等说明如下：

* `create_model`实例化文本检测模型（此处以`PP-OCRv4_mobile_det`为例），具体说明如下：
<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
<th>参数类型</th>
<th>可选项</th>
<th>默认值</th>
</tr>
</thead>
<tr>
<td><code>model_name</code></td>
<td>模型名称</td>
<td><code>str</code></td>
<td>所有PaddleX支持的文本检测模型名称</td>
<td>无</td>
</tr>
<tr>
<td><code>model_dir</code></td>
<td>模型存储路径</td>
<td><code>str</code></td>
<td>无</td>
<td>无</td>
</tr>
<tr>
<td><code>device</code></td>
<td>模型推理设备</td>
<td><code>str</code></td>
<td>支持指定GPU具体卡号，如“gpu:0”，其他硬件具体卡号，如“npu:0”，CPU如“cpu”。</td>
<td><code>gpu:0</code></td>
</tr>
<tr>
<td><code>limit_side_len</code></td>
<td>检测的图像边长限制</td>
<td><code>int/None</code></td>
<td>
<ul>
<li><b>int</b>: 大于0的任意整数
<li><b>None</b>: 如果设置为None, 将默认使用PaddleX官方模型配置中的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>limit_type</code></td>
<td>检测的图像边长限制,检测的边长限制类型 </td>
<td><code>str/None</code></td>
<td>
<ul>
<li><b>str</b>: 支持min和max. min表示保证图像最短边不小于det_limit_side_len, max: 表示保证图像最长边不大于limit_side_len
<li><b>None</b>: 如果设置为None, 将默认使用PaddleX官方模型配置中的该参数值</li></li></ul></td>


<td>None</td>
</tr>
<tr>
<td><code>thresh</code></td>
<td>输出的概率图中，得分大于该阈值的像素点才会被认为是文字像素点 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用PaddleX官方模型配置中的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>box_thresh</code></td>
<td>检测结果边框内，所有像素点的平均得分大于该阈值时，该结果会被认为是文字区域 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用PaddleX官方模型配置中的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>unclip_ratio</code></td>
<td>Vatti clipping算法的扩张系数，使用该方法对文字区域进行扩张 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用PaddleX官方模型配置中的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>是否启用高性能推理</td>
<td><code>bool</code></td>
<td>无</td>
<td><code>False</code></td>
</tr>
</table>

* 其中，`model_name` 必须指定，指定 `model_name` 后，默认使用 PaddleX 内置的模型参数，在此基础上，指定 `model_dir` 时，使用用户自定义的模型。

* 调用文本检测模型的 `predict()` 方法进行推理预测，`predict()` 方法参数有 `input`、 `batch_size`、 `limit_side_len`、 `limit_type`、 `thresh`、 `box_thresh`、 `max_candidates`、`unclip_ratio`和`use_dilation`，具体说明如下：

<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
<th>参数类型</th>
<th>可选项</th>
<th>默认值</th>
</tr>
</thead>
<tr>
<td><code>input</code></td>
<td>待预测数据，支持多种输入类型</td>
<td><code>Python Var</code>/<code>str</code>/<code>dict</code>/<code>list</code></td>
<td>
<ul>
  <li><b>Python变量</b>，如<code>numpy.ndarray</code>表示的图像数据</li>
  <li><b>文件路径</b>，如图像文件的本地路径：<code>/root/data/img.jpg</code></li>
  <li><b>URL链接</b>，如图像文件的网络URL：<a href = "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_rec_001.png">示例</a></li>
  <li><b>本地目录</b>，该目录下需包含待预测数据文件，如本地路径：<code>/root/data/</code></li>
  <li><b>列表</b>，列表元素需为上述类型数据，如<code>[numpy.ndarray, numpy.ndarray]</code>，<code>[\"/root/data/img1.jpg\", \"/root/data/img2.jpg\"]</code>，<code>[\"/root/data1\", \"/root/data2\"]</code></li>
</ul>
</td>
<td>无</td>
</tr>
<tr>
<td><code>batch_size</code></td>
<td>批大小</td>
<td><code>int</code></td>
<td>大于0的任意整数</td>
<td>1</td>
</tr>
<tr>
<td><code>limit_side_len</code></td>
<td>检测的图像边长限制</td>
<td><code>int/None</code></td>
<td>
<ul>
<li><b>int</b>: 大于0的任意整数
<li><b>None</b>: 如果设置为None, 将默认使用模型初始化的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>limit_type</code></td>
<td>检测的图像边长限制,检测的边长限制类型 </td>
<td><code>str/None</code></td>
<td>
<ul>
<li><b>str</b>: 支持min和max. min表示保证图像最短边不小于det_limit_side_len, max: 表示保证图像最长边不大于limit_side_len
<li><b>None</b>: 如果设置为None, 将默认使用模型初始化的该参数值</li></li></ul></td>


<td>None</td>
</tr>
<tr>
<td><code>thresh</code></td>
<td>输出的概率图中，得分大于该阈值的像素点才会被认为是文字像素点 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用模型初始化的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>box_thresh</code></td>
<td>检测结果边框内，所有像素点的平均得分大于该阈值时，该结果会被认为是文字区域 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用模型初始化的该参数值</li></li></ul></td>

<td>None</td>
</tr>
<tr>
<td><code>unclip_ratio</code></td>
<td>Vatti clipping算法的扩张系数，使用该方法对文字区域进行扩张 </td>
<td><code>float/None</code></td>
<td>
<ul>
<li><b>float</b>: 大于0的任意浮点数
<li><b>None</b>: 如果设置为None, 将默认使用模型初始化的该参数值</li></li></ul></td>

<td>None</td>
</tr>
</table>

* 对预测结果进行处理，每个样本的预测结果均为对应的Result对象，且支持打印、保存为图片、保存为`json`文件的操作:

<table>
<thead>
<tr>
<th>方法</th>
<th>方法说明</th>
<th>参数</th>
<th>参数类型</th>
<th>参数说明</th>
<th>默认值</th>
</tr>
</thead>
<tr>
<td rowspan="3"><code>print()</code></td>
<td rowspan="3">打印结果到终端</td>
<td><code>format_json</code></td>
<td><code>bool</code></td>
<td>是否对输出内容进行使用 <code>JSON</code> 缩进格式化</td>
<td><code>True</code></td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>指定缩进级别，以美化输出的 <code>JSON</code> 数据，使其更具可读性，仅当 <code>format_json</code> 为 <code>True</code> 时有效</td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>控制是否将非 <code>ASCII</code> 字符转义为 <code>Unicode</code>。设置为 <code>True</code> 时，所有非 <code>ASCII</code> 字符将被转义；<code>False</code> 则保留原始字符，仅当<code>format_json</code>为<code>True</code>时有效</td>
<td><code>False</code></td>
</tr>
<tr>
<td rowspan="3"><code>save_to_json()</code></td>
<td rowspan="3">将结果保存为json格式的文件</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致</td>
<td>无</td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>指定缩进级别，以美化输出的 <code>JSON</code> 数据，使其更具可读性，仅当 <code>format_json</code> 为 <code>True</code> 时有效</td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>控制是否将非 <code>ASCII</code> 字符转义为 <code>Unicode</code>。设置为 <code>True</code> 时，所有非 <code>ASCII</code> 字符将被转义；<code>False</code> 则保留原始字符，仅当<code>format_json</code>为<code>True</code>时有效</td>
<td><code>False</code></td>
</tr>
<tr>
<td><code>save_to_img()</code></td>
<td>将结果保存为图像格式的文件</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>保存的文件路径，当为目录时，保存文件命名与输入文件类型命名一致</td>
<td>无</td>
</tr>
</table>

* 此外，也支持通过属性获取带结果的可视化图像和预测结果，具体如下：

<table>
<thead>
<tr>
<th>属性</th>
<th>属性说明</th>
</tr>
</thead>
<tr>
<td rowspan="1"><code>json</code></td>
<td rowspan="1">获取预测的<code>json</code>格式的结果</td>
</tr>
<tr>
<td rowspan="1"><code>img</code></td>
<td rowspan="1">获取格式为<code>dict</code>的可视化图像</td>
</tr>
</table>


关于更多 PaddleX 的单模型推理的 API 的使用方法，可以参考 [PaddleX单模型Python脚本使用说明](../../../module_usage/instructions/model_python_API.md)。

## 四、二次开发
如果你追求更高精度的现有模型，可以使用 PaddleX 的二次开发能力开发更好的文本检测模型。在使用 PaddleX 开发文本检测模型之前，请务必安装 PaddleX 的 PaddleOCR 插件，安装过程可以参考 [PaddleX本地安装教程](../../../installation/installation.md)。

### 4.1 数据准备
在进行模型训练前，需要准备相应任务模块的数据集。PaddleX 针对每一个模块提供了数据校验功能，<b>只有通过数据校验的数据才可以进行模型训练</b>。
此外，PaddleX 为每一个模块都提供了 Demo 数据集，您可以基于官方提供的 Demo 数据完成后续的开发。若您希望用私有数据集进行后续的模型训练，可以参考 [PaddleX文本检测/文本识别任务模块数据标注教程](../../../data_annotations/ocr_modules/text_detection_recognition.md)。

#### 4.1.1 Demo 数据下载

您可以参考下面的命令将 Demo 数据集下载到指定文件夹：

```bash
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ocr_det_dataset_examples.tar -P ./dataset
tar -xf ./dataset/ocr_det_dataset_examples.tar -C ./dataset/
```
#### 4.1.2 数据校验

一行命令即可完成数据校验：

```bash
python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/ocr_det_dataset_examples
```
执行上述命令后，PaddleX 会对数据集进行校验，并统计数据集的基本信息，命令运行成功后会在log中打印出`Check dataset passed !`信息。校验结果文件保存在`./output/check_dataset_result.json`，同时相关产出会保存在当前目录的`./output/check_dataset`目录下，产出目录中包括可视化的示例样本图片和样本分布直方图。

<details><summary>👉 <b>校验结果详情（点击展开）</b></summary>
<p>校验结果文件具体内容为：</p>
<pre><code class="language-bash">{
  "done_flag": true,
  "check_pass": true,
  "attributes": {
    "train_samples": 200,
    "train_sample_paths": [
      "../dataset/ocr_det_dataset_examples/images/train_img_61.jpg",
      "../dataset/ocr_det_dataset_examples/images/train_img_289.jpg"
    ],
    "val_samples": 50,
    "val_sample_paths": [
      "../dataset/ocr_det_dataset_examples/images/val_img_61.jpg",
      "../dataset/ocr_det_dataset_examples/images/val_img_137.jpg"
    ]
  },
  "analysis": {
    "histogram": "check_dataset/histogram.png"
  },
  "dataset_path": "./dataset/ocr_det_dataset_examples",
  "show_type": "image",
  "dataset_type": "TextDetDataset"
}
</code></pre>
<p>上述校验结果中，<code>check_pass</code> 为 <code>true</code> 表示数据集格式符合要求，其他部分指标的说明如下：</p>
<ul>
<li><code>attributes.train_samples</code>：该数据集训练集样本数量为 200；</li>
<li><code>attributes.val_samples</code>：该数据集验证集样本数量为 50；</li>
<li><code>attributes.train_sample_paths</code>：该数据集训练集样本可视化图片相对路径列表；</li>
<li><code>attributes.val_sample_paths</code>：该数据集验证集样本可视化图片相对路径列表；</li>
</ul>
<p>另外，数据集校验还对数据集中所有图片的长宽分布情况进行了分析分析，并绘制了分布直方图（histogram.png）：</p>
<p><img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/modules/text_det/01.png"/></p></details>

#### 4.1.3 数据集格式转换/数据集划分（可选）

在您完成数据校验之后，可以通过<b>修改配置文件</b>或是<b>追加超参数</b>的方式对数据集的格式进行转换，也可以对数据集的训练/验证比例进行重新划分。

<details><summary>👉 <b>格式转换/数据集划分详情（点击展开）</b></summary>
<p><b>（1）数据集格式转换</b></p>
<p>文本检测不支持数据格式转换。</p>
<p><b>（2）数据集划分</b></p>
<p>数据集划分的参数可以通过修改配置文件中 <code>CheckDataset</code> 下的字段进行设置，配置文件中部分参数的示例说明如下：</p>
<ul>
<li><code>CheckDataset</code>:</li>
<li><code>split</code>:</li>
<li><code>enable</code>: 是否进行重新划分数据集，为 <code>True</code> 时进行数据集格式转换，默认为 <code>False</code>；</li>
<li><code>train_percent</code>: 如果重新划分数据集，则需要设置训练集的百分比，类型为0-100之间的任意整数，需要保证与 <code>val_percent</code> 的值之和为100；</li>
</ul>
<p>例如，您想重新划分数据集为 训练集占比90%、验证集占比10%，则需将配置文件修改为：</p>
<pre><code class="language-bash">......
CheckDataset:
  ......
  split:
    enable: True
    train_percent: 90
    val_percent: 10
  ......
</code></pre>
<p>随后执行命令：</p>
<pre><code class="language-bash">python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/ocr_det_dataset_examples
</code></pre>
<p>数据划分执行之后，原有标注文件会被在原路径下重命名为 <code>xxx.bak</code>。</p>
<p>以上参数同样支持通过追加命令行参数的方式进行设置：</p>
<pre><code class="language-bash">python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml  \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/ocr_det_dataset_examples \
    -o CheckDataset.split.enable=True \
    -o CheckDataset.split.train_percent=90 \
    -o CheckDataset.split.val_percent=10
</code></pre></details>

### 4.2 模型训练
一条命令即可完成模型的训练，以此处 PP-OCRv4 移动端文本检测模型（`PP-OCRv4_mobile_det`）的训练为例：

```bash
python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml \
    -o Global.mode=train \
    -o Global.dataset_dir=./dataset/ocr_det_dataset_examples
```
需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-OCRv4_mobile_det.yaml`，训练其他模型时，需要的指定相应的配置文件，模型和配置的文件的对应关系，可以查阅[PaddleX模型列表（CPU/GPU）](../../../support_list/models_list.md)）
* 指定模式为模型训练：`-o Global.mode=train`
* 指定训练数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Train`下的字段来进行设置，也可以通过在命令行中追加参数来进行调整。如指定前 2 卡 gpu 训练：`-o Global.device=gpu:0,1`；设置训练轮次数为 10：`-o Train.epochs_iters=10`。更多可修改的参数及其详细解释，可以查阅模型对应任务模块的配置文件说明 [PaddleX通用模型配置文件参数说明](../../../module_usage/instructions/config_parameters_common.md)。

<details><summary>👉 <b>更多说明（点击展开）</b></summary>
<ul>
<li>模型训练过程中，PaddleX 会自动保存模型权重文件，默认为<code>output</code>，如需指定保存路径，可通过配置文件中 <code>-o Global.output</code> 字段进行设置。</li>
<li>PaddleX 对您屏蔽了动态图权重和静态图权重的概念。在模型训练的过程中，会同时产出动态图和静态图的权重，在模型推理时，默认选择静态图权重推理。</li>
<li>
<p>在完成模型训练后，所有产出保存在指定的输出目录（默认为<code>./output/</code>）下，通常有以下产出：</p>
</li>
<li>
<p><code>train_result.json</code>：训练结果记录文件，记录了训练任务是否正常完成，以及产出的权重指标、相关文件路径等；</p>
</li>
<li><code>train.log</code>：训练日志文件，记录了训练过程中的模型指标变化、loss 变化等；</li>
<li><code>config.yaml</code>：训练配置文件，记录了本次训练的超参数的配置；</li>
<li><code>.pdparams</code>、<code>.pdema</code>、<code>.pdopt.pdstate</code>、<code>.pdiparams</code>、<code>.pdmodel</code>：模型权重相关文件，包括网络参数、优化器、EMA、静态图网络参数、静态图网络结构等；</li>
</ul></details>

### <b>4.3 模型评估</b>
在完成模型训练后，可以对指定的模型权重文件在验证集上进行评估，验证模型精度。使用 PaddleX 进行模型评估，一条命令即可完成模型的评估：

```bash
python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml \
    -o Global.mode=evaluate \
    -o Global.dataset_dir=./dataset/ocr_det_dataset_examples
```
与模型训练类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-OCRv4_mobile_det.yaml`）
* 指定模式为模型评估：`-o Global.mode=evaluate`
* 指定验证数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Evaluate`下的字段来进行设置，详细请参考 [PaddleX通用模型配置文件参数说明](../../../module_usage/instructions/config_parameters_common.md)。


<details><summary>👉 <b>更多说明（点击展开）</b></summary>
<p>在模型评估时，需要指定模型权重文件路径，每个配置文件中都内置了默认的权重保存路径，如需要改变，只需要通过追加命令行参数的形式进行设置即可，如<code>-o Evaluate.weight_path=./output/best_accuracy/best_accuracy.pdparams</code>。</p>
<p>在完成模型评估后，会产出<code>evaluate_result.json</code>，其记录了评估的结果，具体来说，记录了评估任务是否正常完成，以及模型的评估指标，包含 <code>precision</code>、<code>recall</code>、<code>hmean</code>。</p></details>

### <b>4.4 模型推理和模型集成</b>
在完成模型的训练和评估后，即可使用训练好的模型权重进行推理预测或者进行Python集成。

#### 4.4.1 模型推理
通过命令行的方式进行推理预测，只需如下一条命令。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_001.png)到本地。

```bash
python main.py -c paddlex/configs/modules/text_detection/PP-OCRv4_mobile_det.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir="./output/best_accuracy/inference" \
    -o Predict.input="general_ocr_001.png"
```
与模型训练和评估类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`PP-OCRv4_mobile_det.yaml`）
* 指定模式为模型推理预测：`-o Global.mode=predict`
* 指定模型权重路径：`-o Predict.model_dir="./output/best_accuracy/inference"`
* 指定输入数据路径：`-o Predict.input="..."`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Predict`下的字段来进行设置，详细请参考 [PaddleX通用模型配置文件参数说明](../../../module_usage/instructions/config_parameters_common.md)。

* 也可以用 PaddleX 的 wheel 包进行推理，方便地将模型集成到您自己的项目中。
#### 4.4.2 模型集成
模型可以直接集成到 PaddleX 产线中，也可以直接集成到您自己的项目中。

1.<b>产线集成</b>

文本检测模块可以集成的 PaddleX 产线有[通用 OCR 产线](../../../pipeline_usage/tutorials/ocr_pipelines/OCR.md)、[表格识别产线](../../../pipeline_usage/tutorials/ocr_pipelines/table_recognition.md)、[文档场景信息抽取v3产线（PP-ChatOCRv3-doc）](../../../pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction_v3.md)，只需要替换模型路径即可完成相关产线的文本检测模块的模型更新。

2.<b>模块集成</b>

您产出的权重可以直接集成到文本检测模块中，可以参考[快速集成](#三快速集成)的 Python 示例代码，只需要将模型替换为你训练的到的模型路径即可。

您也可以利用 PaddleX 高性能推理插件来优化您模型的推理过程，进一步提升效率，详细的流程请参考[PaddleX高性能推理指南](../../../pipeline_deploy/high_performance_inference.md)。
