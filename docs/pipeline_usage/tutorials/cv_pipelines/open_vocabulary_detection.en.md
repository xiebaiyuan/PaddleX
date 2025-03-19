---
comments: true
---

# Open Vocabulary Detection Pipeline Tutorial

## 1. Introduction to Open Vocabulary Detection Pipeline
Open vocabulary object detection is an advanced object detection technology that aims to overcome the limitations of traditional object detection. Traditional methods can only recognize objects of predefined categories, while open vocabulary object detection allows the model to recognize objects that did not appear during training. By combining natural language processing techniques, new categories can be defined using text descriptions, enabling the model to recognize and locate these new objects. This makes object detection more flexible and generalizable, with significant application prospects. This pipeline also provides flexible service deployment options, supporting multiple programming languages on various hardware. Currently, this pipeline does not support custom development of the model, but it is planned to be supported in the future.

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/modules/open_vocabulary_detection/open_vocabulary_detection_res.jpg">

<b>The general open vocabulary detection pipeline includes an open vocabulary detection module. You can choose the model based on the benchmark data below.</b>

<b>If you prioritize model accuracy, choose a model with higher accuracy; if you prioritize inference speed, choose a model with faster inference speed; if you prioritize storage size, choose a model with a smaller storage size.</b>

<p><b>General Image Open Vocabulary Detection Module (Optional):</b></p>

<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>mAP(0.5:0.95)</th>
<th>mAP(0.5)</th>
<th>GPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
<tr>
<td>GroundingDINO-T</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0b2/GroundingDINO-T_infer.tar">Inference Model</a></td>
<td>49.4</td>
<td>64.4</td>
<td>253.72</td>
<td>1807.4</td>
<td>658.3</td>
<td rowspan="3">An open vocabulary object detection model trained on O365, GoldG, and Cap4M datasets. The text encoder uses Bert, and the visual model part adopts DINO overall, with additional cross-modal fusion modules designed, achieving good results in the field of open vocabulary object detection.</td>
</tr>
</table>
<strong>Test Environment Description:</strong>

  <ul>
      <li><b>Performance Test Environment</b>
          <ul>
            <li><strong>Test Dataset：</strong>COCO val2017 validation set</li>
              <li><strong>Hardware Configuration：</strong>
                  <ul>
                      <li>GPU: NVIDIA Tesla T4</li>
                      <li>CPU: Intel Xeon Gold 6271C @ 2.60GHz</li>
                      <li>Other Environments: Ubuntu 20.04 / cuDNN 8.6 / TensorRT 8.5.2.2</li>
                  </ul>
              </li>
          </ul>
      </li>
      <li><b>Inference Mode Description</b></li>
  </ul>

<table border="1">
    <thead>
        <tr>
            <th>Mode</th>
            <th>GPU Configuration </th>
            <th>CPU Configuration </th>
            <th>Acceleration Technology Combination</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Normal Mode</td>
            <td>FP32 Precision / No TRT Acceleration</td>
            <td>FP32 Precision / 8 Threads</td>
            <td>PaddleInference</td>
        </tr>
        <tr>
            <td>High-Performance Mode</td>
            <td>Optimal combination of pre-selected precision types and acceleration strategies</td>
            <td>FP32 Precision / 8 Threads</td>
            <td>Pre-selected optimal backend (Paddle/OpenVINO/TRT, etc.)</td>
        </tr>
    </tbody>
</table>

## 2. Quick Start

### 2.1 Local Experience
> ❗ Before using the general open vocabulary detection pipeline locally, please ensure that you have completed the installation of the PaddleX wheel package according to the [PaddleX Local Installation Guide](../../../installation/installation.md).

#### 2.1.1 Command Line Experience
* You can quickly experience the open vocabulary detection pipeline with a single command. Use the [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/open_vocabulary_detection.jpg) and replace `--input` with your local path for prediction.

Due to network issues, the above web page parsing was not successful. If you need the content of the web page, please check the validity of the web page link and try again. If you do not need the parsing of this link, you can proceed with other questions.

```bash
paddlex --pipeline open_vocabulary_detection \
        --input open_vocabulary_detection.jpg \
        --prompt "bus . walking man . rearview mirror ." \
        --thresholds "{'text_threshold': 0.25, 'box_threshold': 0.3}" \
        --save_path ./output \
        --device gpu:0
```

The relevant parameter description can be found in the parameter description in [2.1.2 Integration via Python Script]().

After running, the result will be printed to the terminal, as follows:

```bash
{'res': {'input_path': 'open_vocabulary_detection.jpg', 'page_index': None, 'boxes': [{'coordinate': [112.10542297363281, 117.93667602539062, 514.35693359375, 382.10150146484375], 'label': 'bus', 'score': 0.9348853230476379}, {'coordinate': [264.1828918457031, 162.6674346923828, 286.8844909667969, 201.86187744140625], 'label': 'rearview mirror', 'score': 0.6022508144378662}, {'coordinate': [606.1133422851562, 254.4973907470703, 622.56982421875, 293.7867126464844], 'label': 'walking man', 'score': 0.4384709894657135}, {'coordinate': [591.8192138671875, 260.2451171875, 607.3953247070312, 294.2210388183594], 'label': 'man', 'score': 0.3573091924190521}]}}
```

The explanation of the running result parameters can refer to the result explanation in [2.1.2 Python Script Integration](#212-python-script-integration).

The visualization results are saved under `save_path`, and the visualization results of open vocabulary detection are as follows:

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/modules/open_vocabulary_detection/open_vocabulary_detection_res.jpg">

#### 2.1.2 Python Script Integration
* The above command line is for quickly experiencing the effect. Generally, in a project, it is often necessary to integrate through code. You can complete the rapid inference of the pipeline with just a few lines of code. The inference code is as follows:

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline_name="open_vocabulary_detection")
output = pipeline.predict(input="open_vocabulary_detection.jpg", prompt="bus . walking man . rearview mirror .")
for res in output:
    res.print()
    res.save_to_img(save_path="./output/")
    res.save_to_json(save_path="./output/")
```

In the above Python script, the following steps are executed:

(1) The <code>create_pipeline()</code> function is used to instantiate an Open Vocabulary Detection pipeline object, with the specific parameter descriptions as follows:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Parameter Description</th>
<th>Parameter Type</th>
<th>Default Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pipeline_name</code></td>
<td>The name of the pipeline, which must be supported by PaddleX.</td>
<td><code>str</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>config</code></td>
<td>The path to the pipeline configuration file.</td>
<td><code>str</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>The inference device for the pipeline. It supports specifying the exact card number for GPU, such as "gpu:0", other hardware card numbers, such as "npu:0", or CPU, such as "cpu".</td>
<td><code>str</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>Whether to enable high-performance inference, which is only available if the pipeline supports high-performance inference.</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>

(2) The <code>predict()</code> method of the Open Vocabulary Detection pipeline object is called to perform inference prediction. This method returns a <code>generator</code>. Below are the parameters and their descriptions for the <code>predict()</code> method:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Parameter Description</th>
<th>Parameter Type</th>
<th>Options</th>
<th>Default Value</th>
</tr>
</thead>
<tr>
<td><code>input</code></td>
<td>The data to be predicted, supporting multiple input types (required).</td>
<td><code>Python Var|str|list</code></td>
<td>
<ul>
  <li><b>Python Var</b>: Image data represented by <code>numpy.ndarray</code>.</li>
  <li><b>str</b>: Local path of an image file or PDF file, such as <code>/root/data/img.jpg</code>; <b>URL link</b>, such as the network URL of an image file or PDF file: <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/open_vocabulary_detection.jpg">example</a>; <b>Local directory</b>, which must contain images to be predicted, such as the local path: <code>/root/data/</code> (currently, prediction of PDF files in directories is not supported; PDF files must be specified with an exact file path).</li>
  <li><b>List</b>: The elements of the list must be of the above types, such as <code>[numpy.ndarray, numpy.ndarray]</code>, <code>["/root/data/img1.jpg", "/root/data/img2.jpg"]</code>, <code>["/root/data1", "/root/data2"]</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>The inference device for the pipeline.</td>
<td><code>str|None</code></td>
<td>
<ul>
  <li><b>CPU</b>: For example, <code>cpu</code> indicates using the CPU for inference;</li>
  <li><b>GPU</b>: For example, <code>gpu:0</code> indicates using the first GPU for inference;</li>
  <li><b>NPU</b>: For example, <code>npu:0</code> indicates using the first NPU for inference;</li>
  <li><b>XPU</b>: For example, <code>xpu:0</code> indicates using the first XPU for inference;</li>
  <li><b>MLU</b>: For example, <code>mlu:0</code> indicates using the first MLU for inference;</li>
  <li><b>DCU</b>: For example, <code>dcu:0</code> indicates using the first DCU for inference;</li>
  <li><b>None</b>: If set to <code>None</code>, the parameter value initialized by the pipeline will be used by default. During initialization, the local GPU device 0 will be prioritized; if unavailable, the CPU device will be used.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>thresholds</code></td>
<td>The thresholds used during model inference.</td>
<td><code>dict[str, float]</code></td>
<td>
<ul>
    <li><b>dict[str, float]</b>: The key is a string representing the threshold name, and the value is a floating-point number between 0 and 1, representing the threshold value. For example, for GroundingDINO, the setting is <code>{"text_threshold": 0.25, "box_threshold": 0.3}</code>, which means the text threshold for GroundingDINO is set to 0.25, and the object detection box threshold is set to 0.3.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>prompt</code></td>
<td>The prompt used during model inference.</td>
<td><code>str</code></td>
<td>
<ul>
    <li><b>str</b>: This must be set according to the specific model. For example, for GroundingDINO, the prompt is <code>"{category1} . {category2} . {category3} ."</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
</table>

(3) Process the prediction results. The prediction result for each sample is of the `dict` type and supports operations such as printing, saving as an image, and saving as a `json` file:

<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
<th>Parameter</th>
<th>Parameter Type</th>
<th>Parameter Description</th>
<th>Default Value</th>
</tr>
</thead>
<tr>
<td rowspan = "3"><code>print()</code></td>
<td rowspan = "3">Print the result to the terminal</td>
<td><code>format_json</code></td>
<td><code>bool</code></td>
<td>Whether to format the output content using <code>JSON</code> indentation</td>
<td><code>True</code></td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>Specify the indentation level to beautify the output <code>JSON</code> data, making it more readable. Effective only when <code>format_json</code> is <code>True</code></td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>Control whether to escape non-<code>ASCII</code> characters to <code>Unicode</code>. When set to <code>True</code>, all non-<code>ASCII</code> characters will be escaped; <code>False</code> will retain the original characters. Effective only when <code>format_json</code> is <code>True</code></td>
<td><code>False</code></td>
</tr>
<tr>
<td rowspan = "3"><code>save_to_json()</code></td>
<td rowspan = "3">Save the result as a JSON file</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>Path to save the file. When it is a directory, the saved file name is consistent with the input file type naming</td>
<td>None</td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>Specify the indentation level to beautify the output <code>JSON</code> data, making it more readable. Effective only when <code>format_json</code> is <code>True</code></td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>Control whether to escape non-<code>ASCII</code> characters to <code>Unicode</code>. When set to <code>True</code>, all non-<code>ASCII</code> characters will be escaped; <code>False</code> will retain the original characters. Effective only when <code>format_json</code> is <code>True</code></td>
<td><code>False</code></td>
</tr>
<tr>
<td><code>save_to_img()</code></td>
<td>Save the result as an image file</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>Path to save the file, supports directory or file path</td>
<td>None</td>
</tr>
</table>

- Calling the `print()` method will print the result to the terminal, with the printed content explained as follows:

    - `input_path`: `(str)` The input path of the image to be predicted

    - `page_index`: `(Union[int, None])` If the input is a PDF file, it indicates which page of the PDF it is, otherwise it is `None`

    - `boxes`: `(list)` Detection box information, each element is a dictionary containing the following fields
      - `label`: `(str)` Category name
      - `score`: `(float)` Confidence score
      - `coordinates`: `(list)` Detection box coordinates, in the format `[xmin, ymin, xmax, ymax]`

- Calling the `save_to_json()` method will save the above content to the specified `save_path`. If specified as a directory, the saved path will be `save_path/{your_img_basename}_res.json`; if specified as a file, it will be saved directly to that file. Since JSON files do not support saving numpy arrays, the `numpy.array` types will be converted to lists.

- Calling the `save_to_img()` method will save the visualization results to the specified `save_path`. If specified as a directory, the saved path will be `save_path/{your_img_basename}_res.{your_img_extension}`; if specified as a file, it will be saved directly to that file.

* Additionally, it also supports obtaining visualized images and prediction results through attributes, as follows:

<table>
<thead>
<tr>
<th>Attribute</th>
<th>Attribute Description</th>
</tr>
</thead>
<tr>
<td rowspan = "1"><code>json</code></td>
<td rowspan = "1">Get the predicted <code>json</code> format result</td>
</tr>
<tr>
<td rowspan = "2"><code>img</code></td>
<td rowspan = "2">Get the visualized image in <code>dict</code> format</td>
</tr>
</table>

- The prediction result obtained by the `json` attribute is a dict type of data, with content consistent with the content saved by calling the `save_to_json()` method.
- The prediction result returned by the `img` attribute is a dictionary type of data. The key is `res`, and the corresponding value is an `Image.Image` object used for visualizing the open vocabulary detection results.

In addition, you can obtain the open vocabulary detection pipeline configuration file and load the configuration file for prediction. You can execute the following command to save the result in `my_path`:

```
paddlex --get_pipeline_config open_vocabulary_detection --save_path ./my_path
```

If you have obtained the configuration file, you can customize the settings for the open vocabulary detection pipeline. Simply modify the value of the `pipeline` parameter in the `create_pipeline` method to the path of the pipeline configuration file. An example is as follows:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="./my_path/open_vocabulary_detection.yaml")

output = pipeline.predict(
    input="./open_vocabulary_detection.jpg",
    thresholds={"text_threshold": 0.25, "box_threshold": 0.3},
    prompt="cat . dog . bird ."
)
for res in output:
    res.print()
    res.save_to_img("./output/")
    res.save_to_json("./output/")

```

<b>Note:</b> The parameters in the configuration file are for pipeline initialization. If you wish to change the initialization parameters of the general open vocabulary detection pipeline, you can directly modify the parameters in the configuration file and load the configuration file for prediction. Additionally, CLI prediction also supports passing in the configuration file by specifying the path with `--pipeline`.

## 3. Development Integration/Deployment
If the pipeline meets your requirements for inference speed and accuracy, you can proceed directly with development integration/deployment.

If you need to apply the pipeline directly to your Python project, you can refer to the example code in [2.1.2 Python Script Integration](#212-python-script-integration).

Additionally, PaddleX provides three other deployment methods, detailed as follows:

🚀 <b>High-Performance Inference</b>: In actual production environments, many applications have stringent standards for the performance metrics of deployment strategies (especially response speed) to ensure efficient system operation and smooth user experience. For this purpose, PaddleX provides a high-performance inference plugin, aimed at deeply optimizing the performance of model inference and pre/post-processing, significantly accelerating the end-to-end process. For detailed high-performance inference procedures, please refer to [PaddleX High-Performance Inference Guide](../../../pipeline_deploy/high_performance_inference.md).

☁️ <b>Service Deployment</b>: Service deployment is a common form of deployment in actual production environments. By encapsulating the inference function as a service, clients can access these services via network requests to obtain inference results. PaddleX supports multiple pipeline service deployment solutions. For detailed pipeline service deployment procedures, please refer to [PaddleX Service Deployment Guide](../../../pipeline_deploy/serving.md).

Below are the API references and multi-language service invocation examples for basic service deployment:

<details><summary>API Reference</summary>

<p>For the main operations provided by the service:</p>
<ul>
<li>The HTTP request method is POST.</li>
<li>Both the request body and response body are JSON data (JSON objects).</li>
<li>When the request is processed successfully, the response status code is <code>200</code>, and the response body has the following attributes:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>The UUID of the request.</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Fixed at <code>0</code>.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error description. Fixed at <code>"Success"</code>.</td>
</tr>
<tr>
<td><code>result</code></td>
<td><code>object</code></td>
<td>Operation result.</td>
</tr>
</tbody>
</table>
<ul>
<li>When the request is not processed successfully, the response body has the following attributes:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>The UUID of the request.</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Same as the response status code.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error description.</td>
</tr>
</tbody>
</table>
<p>The main operations provided by the service are as follows:</p>
<ul>
<li><b><code>infer</code></b></li>
</ul>
<p>Perform object detection on an image.</p>
<p><code>POST /open-vocabulary-detection</code></p>
<ul>
<li>The attributes of the request body are as follows:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Meaning</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td><code>string</code></td>
<td>The URL of the image file accessible by the server or the Base64 encoded result of the image file content.</td>
<td>Yes</td>
</tr>
<tr>
<td><code>prompt</code></td>
<td><code>string</code></td>
<td>The text prompt used for prediction.</td>
<td>Yes</td>
</tr>
<tr>
<td><code>thresholds</code></td>
<td><code>object</code> | <code>null</code></td>
<td>The thresholds used by the model for prediction.</td>
<td>No</td>
</tr>
</tbody>
</table>
<ul>
<li>When the request is processed successfully, the <code>result</code> in the response body has the following attributes:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>detectedObjects</code></td>
<td><code>array</code></td>
<td>Information about the position, category, etc., of the objects.</td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>string</code></td>
<td>The result image of object detection. The image is in JPEG format and encoded in Base64.</td>
</tr>
</tbody>
</table>
<p>Each element in <code>detectedObjects</code> is an <code>object</code> with the following attributes:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>bbox</code></td>
<td><code>array</code></td>
<td>The position of the object. The elements in the array are the x-coordinate of the top-left corner, the y-coordinate of the top-left corner, the x-coordinate of the bottom-right corner, and the y-coordinate of the bottom-right corner, in that order.</td>
</tr>
<tr>
<td><code>categoryName</code></td>
<td><code>string</code></td>
<td>The name of the object category.</td>
</tr>
<tr>
<td><code>score</code></td>
<td><code>number</code></td>
<td>The score of the object.</td>
</tr>
</tbody>
</table>
<p>An example of <code>result</code> is as follows:</p>
<pre><code class="language-json">{
&quot;detectedObjects&quot;: [
{
&quot;bbox&quot;: [
404.4967956542969,
90.15770721435547,
506.2465515136719,
285.4187316894531
],
&quot;categoryName&quot;: "bird",
&quot;score&quot;: 0.7418514490127563
},
{
&quot;bbox&quot;: [
155.33145141601562,
81.10954284667969,
199.71136474609375,
167.4235382080078
],
&quot;categoryName&quot;: "dog",
&quot;score&quot;: 0.7328268885612488
}
],
&quot;image&quot;: &quot;xxxxxx&quot;
}
</code></pre></details>

<details><summary>Multi-language Service Call Examples</summary>

<details>
<summary>Python</summary>


<pre><code class="language-python">import base64
import requests

API_URL = "http://localhost:8080/open-vocabulary-detection" # Service URL
image_path = "./open_vocabulary_detection.jpg"
output_image_path = "./out.jpg"

# Base64 encode the local image
with open(image_path, "rb") as file:
    image_bytes = file.read()
    image_data = base64.b64encode(image_bytes).decode("ascii")

payload = {"image": image_data, "prompt": "walking man . bus ."}  # Base64 encoded file content or image URL

# Call the API
response = requests.post(API_URL, json=payload)

# Handle the response data
assert response.status_code == 200, f"{response.status_code}"
result = response.json()["result"]
with open(output_image_path, "wb") as file:
    file.write(base64.b64decode(result["image"]))
print(f"Output image saved at {output_image_path}")
print("\nDetected objects:")
print(result["detectedObjects"])
</code></pre></details>

<details><summary>C++</summary>

<pre><code class="language-cpp">#include &lt;iostream&gt;
#include &quot;cpp-httplib/httplib.h&quot; // <url id="cu9q6pqi5970ak6ek5e0" type="url" status="parsed" title="GitHub - Huiyicc/cpp-httplib: A C++ header-only HTTP/HTTPS server and client library" wc="15064">https://github.com/Huiyicc/cpp-httplib</url>
#include &quot;nlohmann/json.hpp&quot; // <url id="cu9q6pqi5970ak6ek5eg" type="url" status="parsed" title="GitHub - nlohmann/json: JSON for Modern C++" wc="80311">https://github.com/nlohmann/json</url>
#include &quot;base64.hpp&quot; // <url id="cu9q6pqi5970ak6ek5f0" type="url" status="parsed" title="GitHub - tobiaslocker/base64: A modern C++ base64 encoder / decoder" wc="2293">https://github.com/tobiaslocker/base64</url>

int main() {
    httplib::Client client(&quot;localhost:8080&quot;);
    const std::string imagePath = &quot;./demo.jpg&quot;;
    const std::string outputImagePath = &quot;./out.jpg&quot;;

    httplib::Headers headers = {
        {&quot;Content-Type&quot;, &quot;application/json&quot;}
    };

    // Base64 encode the local image
    std::ifstream file(imagePath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector&lt;char&gt; buffer(size);
    if (!file.read(buffer.data(), size)) {
        std::cerr &lt;&lt; &quot;Error reading file.&quot; &lt;&lt; std::endl;
        return 1;
    }
    std::string bufferStr(reinterpret_cast&lt;const char*&gt;(buffer.data()), buffer.size());
    std::string encodedImage = base64::to_base64(bufferStr);

    nlohmann::json jsonObj;
    jsonObj[&quot;image&quot;] = encodedImage;
    std::string body = jsonObj.dump();

    // Call the API
    auto response = client.Post(&quot;/small-object-detection&quot;, headers, body, &quot;application/json&quot;);
    // Handle the response data
    if (response &amp;&amp; response-&gt;status == 200) {
        nlohmann::json jsonResponse = nlohmann::json::parse(response-&gt;body);
        auto result = jsonResponse[&quot;result&quot;];

        encodedImage = result[&quot;image&quot;];
        std::string decodedString = base64::from_base64(encodedImage);
        std::vector&lt;unsigned char&gt; decodedImage(decodedString.begin(), decodedString.end());
        std::ofstream outputImage(outPutImagePath, std::ios::binary | std::ios::out);
        if (outputImage.is_open()) {
            outputImage.write(reinterpret_cast&lt;char*&gt;(decodedImage.data()), decodedImage.size());
            outputImage.close();
            std::cout &lt;&lt; &quot;Output image saved at &quot; &lt;&lt; outPutImagePath &lt;&lt; std::endl;
        } else {
            std::cerr &lt;&lt; &quot;Unable to open file for writing: &quot; &lt;&lt; outPutImagePath &lt;&lt; std::endl;
        }

        auto detectedObjects = result[&quot;detectedObjects&quot;];
        std::cout &lt;&lt; &quot;\nDetected objects:&quot; &lt;&lt; std::endl;
        for (const auto&amp; category : detectedObjects) {
            std::cout &lt;&lt; category &lt;&lt; std::endl;
        }
    } else {
        std::cout &lt;&lt; &quot;Failed to send HTTP request.&quot; &lt;&lt; std::endl;
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
        String API_URL = &quot;http://localhost:8080/small-object-detection&quot;; // Service URL
        String imagePath = &quot;./demo.jpg&quot;; // Local image path
        String outputImagePath = &quot;./out.jpg&quot;; // Output image path

        // Encode the local image in Base64
        File file = new File(imagePath);
        byte[] fileContent = java.nio.file.Files.readAllBytes(file.toPath());
        String imageData = Base64.getEncoder().encodeToString(fileContent);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode params = objectMapper.createObjectNode();
        params.put(&quot;image&quot;, imageData); // Base64-encoded file content or image URL

        // Create an OkHttpClient instance
        OkHttpClient client = new OkHttpClient();
        MediaType JSON = MediaType.Companion.get(&quot;application/json; charset=utf-8&quot;);
        RequestBody body = RequestBody.Companion.create(params.toString(), JSON);
        Request request = new Request.Builder()
                .url(API_URL)
                .post(body)
                .build();

        // Call the API and process the response data
        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                JsonNode resultNode = objectMapper.readTree(responseBody);
                JsonNode result = resultNode.get(&quot;result&quot;);
                String base64Image = result.get(&quot;image&quot;).asText();
                JsonNode detectedObjects = result.get(&quot;detectedObjects&quot;);

                byte[] imageBytes = Base64.getDecoder().decode(base64Image);
                try (FileOutputStream fos = new FileOutputStream(outputImagePath)) {
                    fos.write(imageBytes);
                }
                System.out.println(&quot;Output image saved at &quot; + outputImagePath);
                System.out.println(&quot;\nDetected objects: &quot; + detectedObjects.toString());
            } else {
                System.err.println(&quot;Request failed with code: &quot; + response.code());
            }
        }
    }
}
</code></pre></details>

<details><summary>Go</summary>

<pre><code class="language-go">package main

import (
    &quot;bytes&quot;
    &quot;encoding/base64&quot;
    &quot;encoding/json&quot;
    &quot;fmt&quot;
    &quot;io/ioutil&quot;
    &quot;net/http&quot;
)

func main() {
    API_URL := &quot;http://localhost:8080/small-object-detection&quot;
    imagePath := &quot;./demo.jpg&quot;
    outputImagePath := &quot;./out.jpg&quot;

    // Encode the local image in Base64
    imageBytes, err := ioutil.ReadFile(imagePath)
    if err != nil {
        fmt.Println(&quot;Error reading image file:&quot;, err)
        return
    }
    imageData := base64.StdEncoding.EncodeToString(imageBytes)

    payload := map[string]string{&quot;image&quot;: imageData} // Base64-encoded file content or image URL
    payloadBytes, err := json.Marshal(payload)
    if err != nil {
        fmt.Println(&quot;Error marshaling payload:&quot;, err)
        return
    }

    // Call the API
    client := &amp;http.Client{}
    req, err := http.NewRequest(&quot;POST&quot;, API_URL, bytes.NewBuffer(payloadBytes))
    if err != nil {
        fmt.Println(&quot;Error creating request:&quot;, err)
        return
    }

    res, err := client.Do(req)
    if err != nil {
        fmt.Println(&quot;Error sending request:&quot;, err)
        return
    }
    defer res.Body.Close()

    // Process the response data
    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println(&quot;Error reading response body:&quot;, err)
        return
    }
    type Response struct {
        Result struct {
            Image      string   `json:&quot;image&quot;`
            DetectedObjects []map[string]interface{} `json:&quot;detectedObjects&quot;`
        } `json:&quot;result&quot;`
    }
    var respData Response
    err = json.Unmarshal([]byte(string(body)), &amp;respData)
    if err != nil {
        fmt.Println(&quot;Error unmarshaling response body:&quot;, err)
        return
    }

    outputImageData, err := base64.StdEncoding.DecodeString(respData.Result.Image)
    if err != nil {
        fmt.Println(&quot;Error decoding base64 image data:&quot;, err)
        return
    }
    err = ioutil.WriteFile(outputImagePath, outputImageData, 0644)
    if err != nil {
        fmt.Println(&quot;Error writing image to file:&quot;, err)
        return
    }
    fmt.Printf(&quot;Image saved at %s.jpg\n&quot;, outputImagePath)
    fmt.Println(&quot;\nDetected objects:&quot;)
    for _, category := range respData.Result.DetectedObjects {
        fmt.Println(category)
    }
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
    static readonly string API_URL = &quot;http://localhost:8080/small-object-detection&quot;;
    static readonly string imagePath = &quot;./demo.jpg&quot;;
    static readonly string outputImagePath = &quot;./out.jpg&quot;;

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();

        // Base64 encode the local image
        byte[] imageBytes = File.ReadAllBytes(imagePath);
        string image_data = Convert.ToBase64String(imageBytes);

        var payload = new JObject{ { &quot;image&quot;, image_data } }; // Base64 encoded file content or image URL
        var content = new StringContent(payload.ToString(), Encoding.UTF8, &quot;application/json&quot;);

        // Call the API
        HttpResponseMessage response = await httpClient.PostAsync(API_URL, content);
        response.EnsureSuccessStatusCode();

        // Process the API response
        string responseBody = await response.Content.ReadAsStringAsync();
        JObject jsonResponse = JObject.Parse(responseBody);

        string base64Image = jsonResponse[&quot;result&quot;][&quot;image&quot;].ToString();
        byte[] outputImageBytes = Convert.FromBase64String(base64Image);

        File.WriteAllBytes(outputImagePath, outputImageBytes);
        Console.WriteLine($&quot;Output image saved at {outputImagePath}&quot;);
        Console.WriteLine(&quot;\nDetected objects:&quot;);
        Console.WriteLine(jsonResponse[&quot;result&quot;][&quot;detectedObjects&quot;].ToString());
    }
}
</code></pre></details>

<details><summary>Node.js</summary>

<pre><code class="language-js">const axios = require('axios');
const fs = require('fs');

const API_URL = 'http://localhost:8080/small-object-detection'
const imagePath = './demo.jpg'
const outputImagePath = &quot;./out.jpg&quot;;

let config = {
   method: 'POST',
   maxBodyLength: Infinity,
   url: API_URL,
   data: JSON.stringify({
    'image': encodeImageToBase64(imagePath)  // Base64 encoded file content or image URL
  })
};

// Base64 encode the local image
function encodeImageToBase64(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString('base64');
}

// Call the API
axios.request(config)
.then((response) =&gt; {
    // Process the API response
    const result = response.data[&quot;result&quot;];
    const imageBuffer = Buffer.from(result[&quot;image&quot;], 'base64');
    fs.writeFile(outputImagePath, imageBuffer, (err) =&gt; {
      if (err) throw err;
      console.log(`Output image saved at ${outputImagePath}`);
    });
    console.log(&quot;\nDetected objects:&quot;);
    console.log(result[&quot;detectedObjects&quot;]);
})
.catch((error) =&gt; {
  console.log(error);
});
</code></pre></details>

<details><summary>PHP</summary>

<pre><code class="language-php">&lt;?php

$API_URL = &quot;http://localhost:8080/small-object-detection&quot;; // Service URL
$image_path = &quot;./demo.jpg&quot;;
$output_image_path = &quot;./out.jpg&quot;;

// Base64 encode the local image
$image_data = base64_encode(file_get_contents($image_path));
$payload = array(&quot;image&quot; =&gt; $image_data); // Base64 encoded file content or image URL

// Call the API
$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// Process the API response
$result = json_decode($response, true)[&quot;result&quot;];
file_put_contents($output_image_path, base64_decode($result[&quot;image&quot;]));
echo &quot;Output image saved at &quot; . $output_image_path . &quot;\n&quot;;
echo &quot;\nDetected objects:\n&quot;;
print_r($result[&quot;detectedObjects&quot;]);

?&gt;
</code></pre></details>
</details>
<br/>

📱 <b>Edge Deployment</b>: Edge deployment is a method of placing computing and data processing capabilities on the user's device itself, allowing the device to process data directly without relying on remote servers. PaddleX supports deploying models on edge devices such as Android. For detailed edge deployment procedures, please refer to the [PaddleX Edge Deployment Guide](../../../pipeline_deploy/edge_deploy.md).
You can choose the appropriate method to deploy the model pipeline according to your needs, and then proceed with subsequent AI application integration.

## 4. Custom Development
The current pipeline temporarily does not support fine-tuning training, only inference integration is supported. Fine-tuning training for this pipeline is planned to be supported in the future.

## 5. Multi-Hardware Support
The current pipeline temporarily only supports GPU and CPU inference. Adaptation to more hardware for this pipeline is planned to be supported in the future.
