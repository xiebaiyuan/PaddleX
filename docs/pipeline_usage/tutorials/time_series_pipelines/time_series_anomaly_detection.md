---
comments: true
---

# 时序异常检测产线使用教程

## 1. 通用时序异常检测产线介绍
时序异常检测是一种识别时间序列数据中异常模式或行为的技术，广泛应用于网络安全、设备监控和金融欺诈检测等领域。它通过分析历史数据中的正常趋势和规律，来发现与预期行为显著不同的事件，例如突然增加的网络流量或异常的交易活动。时序异常检测能够自动识别数据中的异常点，为企业和组织提供实时警报，帮助及时应对潜在风险和问题。这项技术在保障系统稳定性和安全性方面发挥着重要作用。本产线同时提供了灵活的服务化部署方式，支持在多种硬件上使用多种编程语言调用。不仅如此，本产线也提供了二次开发的能力，您可以基于本产线在您自己的数据集上训练调优，训练后的模型也可以无缝集成。

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/05.png">


<b>通用</b><b>时序异常检测</b><b>产线中包含了</b><b>时序异常检测</b><b>模块，如您更考虑模型精度，请选择精度较高的模型，如您更考虑模型推理速度，请选择推理速度较快的模型，如您更考虑模型存储大小，请选择存储大小较小的模型</b>。


<table>
<thead>
<tr>
<th>模型</th><th>模型下载链接</th>
<th>precison</th>
<th>recall</th>
<th>f1_score</th>
<th>模型存储大小（M)</th>
</tr>
</thead>
<tbody>
<tr>
<td>AutoEncoder_ad</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/AutoEncoder_ad_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/AutoEncoder_ad_pretrained.pdparams">训练模型</a></td>
<td>99.36</td>
<td>84.36</td>
<td>91.25</td>
<td>52K</td>
</tr>
<tr>
<td>DLinear_ad</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/DLinear_ad_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/DLinear_ad_pretrained.pdparams">训练模型</a></td>
<td>98.98</td>
<td>93.96</td>
<td>96.41</td>
<td>112K</td>
</tr>
<tr>
<td>Nonstationary_ad</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/Nonstationary_ad_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/Nonstationary_ad_pretrained.pdparams">训练模型</a></td>
<td>98.55</td>
<td>88.95</td>
<td>93.51</td>
<td>1.8M</td>
</tr>
<tr>
<td>PatchTST_ad</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PatchTST_ad_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PatchTST_ad_pretrained.pdparams">训练模型</a></td>
<td>98.78</td>
<td>90.70</td>
<td>94.57</td>
<td>320K</td>
</tr>
</tbody>
</table>

<strong>测试环境说明:</strong>

  <ul>
      <li><b>性能测试环境</b>
          <ul>
           <li><strong>测试数据集：
             </strong>
              <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ts_anomaly_examples.tar">PSM</a> 数据集。
             </li>
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



## 2. 快速开始
PaddleX 所提供的预训练的模型产线均可以快速体验效果，你可以在星河社区体验通用时序异常检测产线的效果，也可以在本地使用命令行或 Python 体验时序异常检测产线的效果。

### 2.1 在线体验
您可以[在线体验](https://aistudio.baidu.com/community/app/105706/webUI?source=appCenter)通用时序异常检测产线的效果，用官方提供的 demo 进行识别，例如：

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/time_series/06.png">

如果您对产线运行的效果满意，可以直接进行集成部署。您可以选择从云端下载部署包，也可以参考[2.2节本地体验](#22-本地体验)中的方法进行本地部署。如果对效果不满意，您可以利用私有数据<b>对产线中的模型进行微调训练</b>。如果您具备本地训练的硬件资源，可以直接在本地开展训练；如果没有，星河零代码平台提供了一键式训练服务，无需编写代码，只需上传数据后，即可一键启动训练任务。

<b>注</b>：由于时序数据和场景紧密相关，时序任务的在线体验官方内置模型仅是在一个特定场景下的模型方案，并非通用方案，不适用其他场景，因此体验方式不支持使用任意的文件来体验官方模型方案效果。但是，在完成自己场景数据下的模型训练之后，可以选择自己训练的模型方案，并使用对应场景的数据进行在线体验。

### 2.2 本地体验
在本地使用通用时序异常检测产线前，请确保您已经按照[PaddleX本地安装教程](../../../installation/installation.md)完成了PaddleX的wheel包安装。

#### 2.2.1 命令行方式体验
一行命令即可快速体验时序异常检测产线效果，使用 [测试文件](https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv)，并将 `--input` 替换为本地路径，进行预测

```bash
paddlex --pipeline ts_anomaly_detection --input ts_ad.csv --device gpu:0 --save_path ./output
```

相关的参数说明可以参考[2.2.2 Python脚本方式集成](#222-python脚本方式集成)中的参数说明。

运行后，会将结果打印到终端上，结果如下：

```
{'input_path': 'ts_ad.csv', 'anomaly':            label
timestamp
220226         0
220227         0
220228         0
220229         0
220230         0
...          ...
220317         1
220318         1
220319         1
220320         1
220321         0

[96 rows x 1 columns]}
```

运行结果参数说明可以参考[2.2.2 Python脚本方式集成](#222-python脚本方式集成)中的结果解释。

时序文件结果保存在`save_path`下。

#### 2.2.2 Python脚本方式集成
上述命令行是为了快速体验查看效果，一般来说，在项目中，往往需要通过代码集成，您可以通过几行代码即可完成产线的快速推理，推理代码如下：

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="ts_anomaly_detection")
output = pipeline.predict("ts_ad.csv")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_csv(save_path="./output/") ## 保存csv格式结果
    res.save_to_json(save_path="./output/") ## 保存json格式结果
```

在上述 Python 脚本中，执行了如下几个步骤：

（1）通过 `create_pipeline()` 实例化产线对象：具体参数说明如下：

<table>
<thead>
<tr>
<th>参数</th>
<th>参数说明</th>
<th>参数类型</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pipeline</code></td>
<td>产线名称或是产线配置文件路径。如为产线名称，则必须为 PaddleX 所支持的产线。</td>
<td><code>str</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>config</code></td>
<td>产线具体的配置信息（如果和<code>pipeline</code>同时设置，优先级高于<code>pipeline</code>，且要求产线名和<code>pipeline</code>一致）。</td>
<td><code>dict[str, Any]</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>产线推理设备。支持指定GPU具体卡号，如“gpu:0”，其他硬件具体卡号，如“npu:0”，CPU如“cpu”。</td>
<td><code>str</code></td>
<td><code>gpu:0</code></td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>是否启用高性能推理，仅当该产线支持高性能推理时可用。</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>

（2）调用 ts_anomaly_detection 产线对象的 `predict()` 方法进行推理预测。该方法将返回一个 `generator`。以下是 `predict()` 方法的参数及其说明：

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
<td>待预测数据，支持多种输入类型，必填</td>
<td><code>Python Var|str|list</code></td>
<td>
<ul>
  <li><b>Python Var</b>：如 <code>pandas.DataFrame</code> 表示的时序数据</li>
  <li><b>str</b>：如时序文件的本地路径：<code>/root/data/ts.csv</code>；<b>如URL链接</b>，如时序文件的网络URL：<a href = "https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv">示例</a>；<b>如本地目录</b>，该目录下需包含待预测时序，如本地路径：<code>/root/data/</code></li>
  <li><b>List</b>：列表元素需为上述类型数据，如<code>[pandas.DataFrame, pandas.DataFrame]</code>，<code>[\"/root/data/ts1.csv\", \"/root/data/ts2.csv\"]</code>，<code>[\"/root/data1\", \"/root/data2\"]</code></li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>产线推理设备</td>
<td><code>str|None</code></td>
<td>
<ul>
  <li><b>CPU</b>：如 <code>cpu</code> 表示使用 CPU 进行推理；</li>
  <li><b>GPU</b>：如 <code>gpu:0</code> 表示使用第 1 块 GPU 进行推理；</li>
  <li><b>NPU</b>：如 <code>npu:0</code> 表示使用第 1 块 NPU 进行推理；</li>
  <li><b>XPU</b>：如 <code>xpu:0</code> 表示使用第 1 块 XPU 进行推理；</li>
  <li><b>MLU</b>：如 <code>mlu:0</code> 表示使用第 1 块 MLU 进行推理；</li>
  <li><b>DCU</b>：如 <code>dcu:0</code> 表示使用第 1 块 DCU 进行推理；</li>
  <li><b>None</b>：如果设置为 <code>None</code>, 将默认使用产线初始化的该参数值，初始化时，会优先使用本地的 GPU 0号设备，如果没有，则使用 CPU 设备；</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
</tbody>
</table>

（3）对预测结果进行处理，每个样本的预测结果均为对应的Result对象，且支持打印、保存为`csv`文件、保存为`json`文件的操作:


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
<td rowspan = "3"><code>print()</code></td>
<td rowspan = "3">打印结果到终端</td>
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
<td rowspan = "3"><code>save_to_json()</code></td>
<td rowspan = "3">将结果保存为json格式的文件</td>
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
<td><code>save_to_csv()</code></td>
<td>将结果保存为时序文件格式的文件</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>保存的文件路径，支持目录或文件路径</td>
<td>无</td>
</tr>
</table>

- 调用`print()` 方法会将结果打印到终端，打印到终端的内容解释如下：
    - `input_path`: `(str)` 待预测时序文件的输入路径
    - `anomaly`: `(Pandas.DataFrame)` 时序异常检测结果，包含样本id和对应的异常检测类别。1为异常，0为正常。

- 调用`save_to_json()` 方法会将上述内容保存到指定的`save_path`中，如果指定为目录，则保存的路径为`save_path/{your_ts_basename}_res.json`，如果指定为文件，则直接保存到该文件中。由于json文件不支持保存numpy数组，因此会将其中的`numpy.array`类型转换为列表形式。
- 调用`save_to_csv()` 方法会将可视化结果保存到指定的`save_path`中，如果指定为目录，则保存的路径为`save_path/{your_ts_basename}_res.csv`，如果指定为文件，则直接保存到该文件中。

* 此外，也支持通过属性获取不同格式的预测结果，具体如下：

<table>
<thead>
<tr>
<th>属性</th>
<th>属性说明</th>
</tr>
</thead>
<tr>
<td rowspan = "1"><code>json</code></td>
<td rowspan = "1">获取预测的 <code>json</code> 格式的结果</td>
</tr>
<tr>
<td rowspan = "2"><code>csv</code></td>
<td rowspan = "2">获取格式为 <code>csv</code> 格式的结果</td>
</tr>
</table>


- `json` 属性获取的预测结果为dict类型的数据，相关内容与调用 `save_to_json()` 方法保存的内容一致。
- `csv` 属性返回的是一个`Pandas.DataFrame`类型数据，保存了时序异常检测结果。

此外，您可以获取 ts_anomaly_detection 产线配置文件，并加载配置文件进行预测。可执行如下命令将结果保存在 `my_path` 中：

```
paddlex --get_pipeline_config ts_anomaly_detection --save_path ./my_path
```

若您获取了配置文件，即可对时序异常检测产线各项配置进行自定义，只需要修改 `create_pipeline` 方法中的 `pipeline` 参数值为产线配置文件路径即可。

例如，若您的配置文件保存在 `./my_path/ts_anomaly_detection.yaml` ，则只需执行：

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/ts_anomaly_detection.yaml")
output = pipeline.predict("ts_ad.csv")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_csv("./output/") ## 保存csv格式结果
    res.save_to_json("./output/") ## 保存json格式结果
```

## 3. 开发集成/部署
如果产线可以达到您对产线推理速度和精度的要求，您可以直接进行开发集成/部署。

若您需要将产线直接应用在您的Python项目中，可以参考 [2.2.2 Python脚本方式](#222-python脚本方式集成)中的示例代码。

此外，PaddleX 也提供了其他三种部署方式，详细说明如下：

🚀 <b>高性能推理</b>：在实际生产环境中，许多应用对部署策略的性能指标（尤其是响应速度）有着较严苛的标准，以确保系统的高效运行与用户体验的流畅性。为此，PaddleX 提供高性能推理插件，旨在对模型推理及前后处理进行深度性能优化，实现端到端流程的显著提速，详细的高性能推理流程请参考[PaddleX高性能推理指南](../../../pipeline_deploy/high_performance_inference.md)。

☁️ <b>服务化部署</b>：服务化部署是实际生产环境中常见的一种部署形式。通过将推理功能封装为服务，客户端可以通过网络请求来访问这些服务，以获取推理结果。PaddleX 支持多种产线服务化部署方案，详细的产线服务化部署流程请参考[PaddleX服务化部署指南](../../../pipeline_deploy/serving.md)。

以下是基础服务化部署的API参考与多语言服务调用示例：

<details><summary>API参考</summary>

<p>对于服务提供的主要操作：</p>
<ul>
<li>HTTP请求方法为POST。</li>
<li>请求体和响应体均为JSON数据（JSON对象）。</li>
<li>当请求处理成功时，响应状态码为<code>200</code>，响应体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>请求的UUID。</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>错误码。固定为<code>0</code>。</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>错误说明。固定为<code>"Success"</code>。</td>
</tr>
<tr>
<td><code>result</code></td>
<td><code>object</code></td>
<td>操作结果。</td>
</tr>
</tbody>
</table>
<ul>
<li>当请求处理未成功时，响应体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>请求的UUID。</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>错误码。与响应状态码相同。</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>错误说明。</td>
</tr>
</tbody>
</table>
<p>服务提供的主要操作如下：</p>
<ul>
<li><b><code>infer</code></b></li>
</ul>
<p>进行时序异常检测。</p>
<p><code>POST /time-series-anomaly-detection</code></p>
<ul>
<li>请求体的属性如下：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
<th>是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td><code>string</code> | <code>null</code></td>
<td>时序异常检测结果图。图像为JPEG格式，使用Base64编码。</td>
</tr>
<tr>
<td><code>csv</code></td>
<td><code>string</code></td>
<td>服务器可访问的CSV文件的URL或CSV文件内容的Base64编码结果。CSV文件需要使用UTF-8编码。</td>
<td>是</td>
</tr>
</tbody>
</table>
<ul>
<li>请求处理成功时，响应体的<code>result</code>具有如下属性：</li>
</ul>
<table>
<thead>
<tr>
<th>名称</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>csv</code></td>
<td><code>string</code></td>
<td>CSV格式的时序异常检测结果。使用UTF-8+Base64编码。</td>
</tr>
</tbody>
</table>
<p><code>result</code>示例如下：</p>
<pre><code class="language-json">{
"csv": "xxxxxx",
"image": "xxxxxx"
}
</code></pre></details>

<details><summary>多语言调用服务示例</summary>

<details>
<summary>Python</summary>


<pre><code class="language-python">import base64
import requests

API_URL = "http://localhost:8080/time-series-anomaly-detection" # 服务URL
csv_path = "./test.csv"
output_image_path = "./out.jpg"
output_csv_path = "./out.csv"

# 对本地CSV文件进行Base64编码
with open(csv_path, "rb") as file:
    csv_bytes = file.read()
    csv_data = base64.b64encode(csv_bytes).decode("ascii")

payload = {"csv": csv_data}

# 调用API
response = requests.post(API_URL, json=payload)

# 处理接口返回数据
assert response.status_code == 200
result = response.json()["result"]
with open(output_image_path, "wb") as f:
    f.write(base64.b64decode(result["image"]))
print(f"Output image saved at  {output_image_path}")
with open(output_csv_path, "wb") as f:
    f.write(base64.b64decode(result["csv"]))
print(f"Output time-series data saved at  {output_csv_path}")
</code></pre></details>

<details><summary>C++</summary>

<pre><code class="language-cpp">#include &lt;iostream&gt;
#include "cpp-httplib/httplib.h" // https://github.com/Huiyicc/cpp-httplib
#include "nlohmann/json.hpp" // https://github.com/nlohmann/json
#include "base64.hpp" // https://github.com/tobiaslocker/base64

int main() {
    httplib::Client client("localhost:8080");
    const std::string csvPath = "./test.csv";
    const std::string outputImagePath = "./out.jpg";
    const std::string outputCsvPath = "./out.csv";

    httplib::Headers headers = {
        {"Content-Type", "application/json"}
    };

    // 进行Base64编码
    std::ifstream file(csvPath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector&lt;char&gt; buffer(size);
    if (!file.read(buffer.data(), size)) {
        std::cerr &lt;&lt; "Error reading file." &lt;&lt; std::endl;
        return 1;
    }
    std::string bufferStr(reinterpret_cast&lt;const char*&gt;(buffer.data()), buffer.size());
    std::string encodedCsv = base64::to_base64(bufferStr);

    nlohmann::json jsonObj;
    jsonObj["csv"] = encodedCsv;
    std::string body = jsonObj.dump();

    // 调用API
    auto response = client.Post("/time-series-anomaly-detection", headers, body, "application/json");
    // 处理接口返回数据
    if (response &amp;&amp; response-&gt;status == 200) {
        nlohmann::json jsonResponse = nlohmann::json::parse(response-&gt;body);
        auto result = jsonResponse["result"];

        // 保存数据
        std::string encodedImage = result["image"];
        std::string decodedString = base64::from_base64(encodedImage);
        std::vector<unsigned char> decodedImage(decodedString.begin(), decodedString.end());
        std::ofstream outputImage(outputImagePath, std::ios::binary | std::ios::out);
        if (outputImage.is_open()) {
            outputImage.write(reinterpret_cast<char*>(decodedImage.data()), decodedImage.size());
            outputImage.close();
            std::cout << "Output image data saved at " << outputImagePath << std::endl;
        } else {
            std::cerr << "Unable to open file for writing: " << outputImagePath << std::endl;
        }

        encodedCsv = result["csv"];
        decodedString = base64::from_base64(encodedCsv);
        std::vector&lt;unsigned char&gt; decodedCsv(decodedString.begin(), decodedString.end());
        std::ofstream outputCsv(outputCsvPath, std::ios::binary | std::ios::out);
        if (outputCsv.is_open()) {
            outputCsv.write(reinterpret_cast&lt;char*&gt;(decodedCsv.data()), decodedCsv.size());
            outputCsv.close();
            std::cout &lt;&lt; "Output time-series data saved at " &lt;&lt; outputCsvPath &lt;&lt; std::endl;
        } else {
            std::cerr &lt;&lt; "Unable to open file for writing: " &lt;&lt; outputCsvPath &lt;&lt; std::endl;
        }
    } else {
        std::cout &lt;&lt; "Failed to send HTTP request." &lt;&lt; std::endl;
        std::cout &lt;&lt; response-&gt;body &lt;&lt; std::endl;
        return 1;
    }

    return 0;
}
</code></pre></details>

<details><summary>Java</summary>

<pre><code class="language-java">import okhttp3.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws IOException {
        String API_URL = "http://localhost:8080/time-series-anomaly-detection";
        String csvPath = "./test.csv";
        String outputImagePath = "./out.jpg";
        String outputCsvPath = "./out.csv";

        // 对本地csv进行Base64编码
        File file = new File(csvPath);
        byte[] fileContent = java.nio.file.Files.readAllBytes(file.toPath());
        String csvData = Base64.getEncoder().encodeToString(fileContent);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode params = objectMapper.createObjectNode();
        params.put("csv", csvData);

        // 创建 OkHttpClient 实例
        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.Companion.get("application/json; charset=utf-8");
        RequestBody body = RequestBody.Companion.create(params.toString(), JSON);
        Request request = new Request.Builder()
                .url(API_URL)
                .post(body)
                .build();

        // 调用API并处理接口返回数据
        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                JsonNode resultNode = objectMapper.readTree(responseBody);
                JsonNode result = resultNode.get("result");

                // 保存返回的数据
                String base64Image = result.get("image").asText();
                byte[] imageBytes = Base64.getDecoder().decode(base64Image);
                try (FileOutputStream fos = new FileOutputStream(outputImagePath)) {
                    fos.write(imageBytes);
                }
                System.out.println("Output image data saved at " + outputImagePath);

                String base64Csv = result.get("csv").asText();
                byte[] csvBytes = Base64.getDecoder().decode(base64Csv);
                try (FileOutputStream fos = new FileOutputStream(outputCsvPath)) {
                    fos.write(csvBytes);
                }
                System.out.println("Output time-series data saved at " + outputCsvPath);
            } else {
                System.err.println("Request failed with code: " + response.code());
            }
        }
    }
}
</code></pre></details>

<details><summary>Go</summary>

<pre><code class="language-go">package main

import (
    "bytes"
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    API_URL := "http://localhost:8080/time-series-anomaly-detection"
    csvPath := "./test.csv";
    outputImagePath := "./out.jpg";
    outputCsvPath := "./out.csv";

    // 读取csv文件并进行Base64编码
    csvBytes, err := ioutil.ReadFile(csvPath)
    if err != nil {
        fmt.Println("Error reading csv file:", err)
        return
    }
    csvData := base64.StdEncoding.EncodeToString(csvBytes)

    payload := map[string]string{"csv": csvData} // Base64编码的文件内容
    payloadBytes, err := json.Marshal(payload)
    if err != nil {
        fmt.Println("Error marshaling payload:", err)
        return
    }

    // 调用API
    client := &amp;http.Client{}
    req, err := http.NewRequest("POST", API_URL, bytes.NewBuffer(payloadBytes))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    res, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer res.Body.Close()

    // 处理返回数据
    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }
    type Response struct {
        Result struct {
            Csv string `json:"csv"`
            Image string `json:"image"`
        } `json:"result"`
    }
    var respData Response
    err = json.Unmarshal([]byte(string(body)), &amp;respData)
    if err != nil {
        fmt.Println("Error unmarshaling response body:", err)
        return
    }

    // 将Base64编码的图片数据解码并保存为文件
    outputImageData, err := base64.StdEncoding.DecodeString(respData.Result.Image)
    if err != nil {
        fmt.Println("Error decoding Base64 image data:", err)
        return
    }
    err = ioutil.WriteFile(outputImagePath, outputImageData, 0644)
    if err != nil {
        fmt.Println("Error writing image to file:", err)
        return
    }
    fmt.Printf("Output image data saved at %s.jpg", outputImagePath)

    // 将Base64编码的csv数据解码并保存为文件
    outputCsvData, err := base64.StdEncoding.DecodeString(respData.Result.Csv)
    if err != nil {
        fmt.Println("Error decoding base64 csv data:", err)
        return
    }
    err = ioutil.WriteFile(outputCsvPath, outputCsvData, 0644)
    if err != nil {
        fmt.Println("Error writing csv to file:", err)
        return
    }
    fmt.Printf("Output time-series data saved at %s.csv", outputCsvPath)
}
</code></pre></details>

<details><summary>C#</summary>

<pre><code class="language-csharp">using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class Program
{
    static readonly string API_URL = "http://localhost:8080/time-series-anomaly-detection";
    static readonly string csvPath = "./test.csv";
    static readonly string outputImagePath = "./out.jpg";
    static readonly string outputCsvPath = "./out.csv";

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();

        // 对本地csv文件进行Base64编码
        byte[] csvBytes = File.ReadAllBytes(csvPath);
        string csvData = Convert.ToBase64String(csvBytes);

        var payload = new JObject{ { "csv", csvData } }; // Base64编码的文件内容
        var content = new StringContent(payload.ToString(), Encoding.UTF8, "application/json");

        // 调用API
        HttpResponseMessage response = await httpClient.PostAsync(API_URL, content);
        response.EnsureSuccessStatusCode();

        // 处理接口返回数据
        string responseBody = await response.Content.ReadAsStringAsync();
        JObject jsonResponse = JObject.Parse(responseBody);

        // 保存图片文件
        string base64Image = jsonResponse["result"]["image"].ToString();
        byte[] outputImageBytes = Convert.FromBase64String(base64Image);
        File.WriteAllBytes(outputImagePath, outputImageBytes);
        Console.WriteLine($"Output image data saved at {outputImagePath}");

        // 保存csv文件
        string base64Csv = jsonResponse["result"]["csv"].ToString();
        byte[] outputCsvBytes = Convert.FromBase64String(base64Csv);
        File.WriteAllBytes(outputCsvPath, outputCsvBytes);
        Console.WriteLine($"Output time-series data saved at {outputCsvPath}");
    }
}
</code></pre></details>

<details><summary>Node.js</summary>

<pre><code class="language-js">const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/time-series-anomaly-detection'
const csvPath = "./test.csv";
const outputImagePath = "./out.jpg";
const outputCsvPath = "./out.csv";

let config = {
   method: 'POST',
   maxBodyLength: Infinity,
   url: API_URL,
   data: JSON.stringify({
    'csv': encodeFileToBase64(csvPath)  // Base64编码的文件内容
  })
};

// 读取csv文件并转换为Base64
function encodeFileToBase64(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString('base64');
}

axios.request(config)
.then((response) =&gt; {
    const result = response.data["result"];

    // 保存图片文件
    const imageBuffer = Buffer.from(result["image"], 'base64');
    fs.writeFile(outputImagePath, imageBuffer, (err) =&gt; {
      if (err) throw err;
      console.log(`Output image data saved at ${outputImagePath}`);
    });

    // 保存csv文件
    const csvBuffer = Buffer.from(result["csv"], 'base64');
    fs.writeFile(outputCsvPath, csvBuffer, (err) =&gt; {
      if (err) throw err;
      console.log(`Output time-series data saved at ${outputCsvPath}`);
    });
})
.catch((error) =&gt; {
  console.log(error);
});
</code></pre></details>

<details><summary>PHP</summary>

<pre><code class="language-php">&lt;?php

$API_URL = "http://localhost:8080/time-series-anomaly-detection"; // 服务URL
$csv_path = "./test.csv";
$output_image_path = "./out.jpg";
$output_csv_path = "./out.csv";

// 对本地csv文件进行Base64编码
$csv_data = base64_encode(file_get_contents($csv_path));
$payload = array("csv" =&gt; $csv_data); // Base64编码的文件内容

// 调用API
$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// 处理接口返回数据
$result = json_decode($response, true)["result"];

file_put_contents($output_image_path, base64_decode($result["image"]));
echo "Output image data saved at " . $output_image_path . "\n";

file_put_contents($output_csv_path, base64_decode($result["csv"]));
echo "Output time-series data saved at " . $output_csv_path . "\n";

?&gt;
</code></pre></details>
</details>
<br/>

📱 <b>端侧部署</b>：端侧部署是一种将计算和数据处理功能放在用户设备本身上的方式，设备可以直接处理数据，而不需要依赖远程的服务器。PaddleX 支持将模型部署在 Android 等端侧设备上，详细的端侧部署流程请参考[PaddleX端侧部署指南](../../../pipeline_deploy/edge_deploy.md)。
您可以根据需要选择合适的方式部署模型产线，进而进行后续的 AI 应用集成。

## 4. 二次开发
如果通用时序异常检测产线提供的默认模型权重在您的场景中，精度或速度不满意，您可以尝试利用<b>您自己拥有的特定领域或应用场景的数据</b>对现有模型进行进一步的<b>微调</b>，以提升通用时序异常检测产线的在您的场景中的识别效果。

### 4.1 模型微调
由于通用时序异常检测产线包含时序异常检测模块，如果模型产线的效果不及预期，那么您需要参考[时序异常检测模块使用教程](https://paddlepaddle.github.io/PaddleX/latest/module_usage/tutorials/time_series_modules/time_series_anomaly_detection.html)中的<b>二次开发</b>章节，使用您的私有数据集对时序异常检测模型进行微调。

### 4.2 模型应用
当您使用私有数据集完成微调训练后，可获得本地模型权重文件。

若您需要使用微调后的模型权重，只需对产线配置文件做修改，将微调后模型权重的本地路径填写至产线配置文件中的 `model_dir` 即可：

```yaml
pipeline_name: ts_anomaly_detection

SubModules:
  TSAnomalyDetection:
    module_name: ts_anomaly_detection
    model_name: DLinear_ad
    model_dir: null  # 此处替换为您训练后得到的模型权重本地路径
    batch_size: 1
```

随后， 参考本地体验中的命令行方式或 Python 脚本方式，加载修改后的产线配置文件即可。

##  5. 多硬件支持
PaddleX 支持英伟达 GPU、昆仑芯 XPU、昇腾 NPU和寒武纪 MLU 等多种主流硬件设备，<b>仅需修改 `--device` 参数</b>即可完成不同硬件之间的无缝切换。

例如，您使用昇腾 NPU 进行时序异常检测产线的推理，使用的 CLI 命令为：

```bash
paddlex --pipeline ts_anomaly_detection --input ts_ad.csv --device npu:0
```

当然，您也可以在 Python 脚本中 `create_pipeline()` 时或者 `predict()` 时指定硬件设备。

若您想在更多种类的硬件上使用通用时序异常检测产线，请参考[PaddleX多硬件使用指南](../../../other_devices_support/multi_devices_use_guide.md)。
