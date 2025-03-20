<p align="center">
  <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/logo.png" width="735" height ="200" alt="PaddleX" align="middle" />
</p>

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202-red.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/Python-3.8~3.12-blue.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Windows%2C%20Mac-orange.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/hardware-CPU%2C%20GPU%2C%20XPU%2C%20NPU%2C%20MLU%2C%20DCU-yellow.svg"></a>
</p>

<h4 align="center">
  <a href=#-why-paddlex->🌟 Features</a> | <a href=https://aistudio.baidu.com/application/center/app?tag=%E5%85%A8%E9%83%A8&flod=86503>>🌐  Online Experience</a>｜<a href=#️-quick-start>🚀  Quick Start</a> | <a href=https://paddlepaddle.github.io/PaddleX/latest/en/index.html> 📖 Documentation</a> | <a href=#-what-can-paddlex-do> 🔥Capabilities</a> | <a href=https://paddlepaddle.github.io/PaddleX/latest/en/support_list/models_list.html> 📋 Models</a>
</h4>

<h5 align="center">
  <a href="README.md">🇨🇳 Simplified Chinese</a> | <a href="README_en.md">🇬🇧 English</a></a>
</h5>

## 🔍 Introduction

PaddleX 3.0 is a low-code development tool for AI models built on the PaddlePaddle framework. It integrates numerous **ready-to-use pre-trained models**, enabling **full-process development** from model training to inference, supporting **a variety of mainstream hardware** both domestic and international, and aiding AI developers in industrial practice.


|                                                            [**Image Classification**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_classification.html)                                                            |                                                            [**Multi-label Image Classification**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.html)                                                            |                                                            [**Object Detection**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/object_detection.html)                                                            |                                                            [**Instance Segmentation**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.html)                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/b302cd7e-e027-4ea6-86d0-8a4dd6d61f39" height="126px" width="180px"> | <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/multilabel_cls.png" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/099e2b00-0bbe-4b20-9c5a-96b69e473bd2" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/09f683b4-27df-4c24-b8a7-84da20fdd182" height="126px" width="180px"> |
|                                                              [**Semantic Segmentation**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.html)                                                               |                                                            [**Image Anomaly Detection**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.html)                                                            |                                                          [**OCR**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/OCR.html)                                                          |                                                          [**Table Recognition**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition.html)                                                          |
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/02637f8c-f248-415b-89ab-1276505f198c" height="126px" width="180px"> | <img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/image_anomaly_detection.png" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1ef48536-48d4-484b-a6fb-0d6631ba2386" height="126px" width="180px"> |  <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/1e798e05-dee7-4b41-9cc4-6708b6014efa" height="126px" width="180px"> |
|                                                              [**PP-ChatOCRv3-doc**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.html)                                                              |                                                            [**Time Series Forecasting**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.html)                                                            |                                                              [**Time Series Anomaly Detection**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.html)                                                              |                                                         [**Time Series Classification**](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.html)                                                         |
| <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/e3d97f4e-ab46-411c-8155-494c61492b0a" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/6e897bf6-35fe-45e6-a040-e9a1a20cfdf2" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/c54c66cc-da4f-4631-877b-43b0fbb192a6" height="126px" width="180px"> | <img src="https://github.com/PaddlePaddle/PaddleX/assets/142379845/0ce925b2-3776-4dde-8ce0-5156d5a2476e" height="126px" width="180px"> |



## 🌟 Why PaddleX ?

  🎨 **Rich Models One-click Call**: Integrate over **200 PaddlePaddle models** covering multiple key areas such as OCR, object detection, and time series forecasting into **19 pipelines**. Experience the model effects quickly through easy Python API calls. Also supports **more than 20 modules** for easy model combination use by developers.

  🚀 **High Efficiency and Low barrier of entry**: Achieve model **full-process development** based on graphical interfaces and unified commands, creating **8 featured model pipelines** that combine large and small models, semi-supervised learning of large models, and multi-model fusion, greatly reducing the cost of iterating models.

  🌐 **Flexible Deployment in Various Scenarios**: Support various deployment methods such as **high-performance inference**, **serving**, and **lite deployment** to ensure efficient operation and rapid response of models in different application scenarios.

  🔧 **Efficient Support for Mainstream Hardware**: Support seamless switching of various mainstream hardware such as NVIDIA GPUs, Kunlun XPU, Ascend NPU, and Cambricon MLU to ensure efficient operation.

## 📣 Recent Updates

🔥🔥 **2025.2.14**, PaddleX v3.0.0rc0 major upgrade. This version fully adapts to PaddlePaddle 3.0rc0, with the following core upgrades:

- **Added 12 high-value pipelines**, launching self-developed **[Layout Parsing v2 Pipeline](docs/pipeline_usage/tutorials/ocr_pipelines/PP-StructureV3.en.md)**, **[PP-ChatOCRv4-doc Pipeline](docs/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction_v4.en.md)**, **[Table Recognition v2 Pipeline](docs/pipeline_usage/tutorials/ocr_pipelines/table_recognition_v2.en.md)**. Additionally, new pipelines for document processing, rotated box detection, open vocabulary detection/segmentation, video analysis, multilingual speech recognition, 3D, and other scenarios have been added.

- **Expanded 48 cutting-edge models**, including the major releases in the OCR field such as **Document Layout Detection Model [PP-DocLayout](docs/module_usage/tutorials/ocr_modules/layout_detection.en.md)**, **Formula Recognition Model [PP-FormulaNet](docs/module_usage/tutorials/ocr_modules/formula_recognition.en.md)**, **Table Structure Recognition Model [SLANeXt](docs/module_usage/tutorials/ocr_modules/table_structure_recognition.en.md)**, **Text Recognition Model [PP-OCRv4_server_rec_doc](docs/module_usage/tutorials/ocr_modules/text_recognition.en.md)**. In the CV field, models for 3D detection, human keypoints, open vocabulary detection/segmentation, and in the speech recognition field, models from the Whisper series, among others.

- **Optimized and upgraded the inference APIs for models and pipelines**, supporting more parameter configurations to enhance the flexibility of model and pipeline inference. [Details](docs/API_change_log/v3.0.0rc.en.md).

- **Expanded hardware support:** added support for Suoyuan GCU (90+ models), and significantly increased the number of models for Ascend NPU/Kunlunxin XPU/Cambricon MLU/Hygon DCU.

- **Upgraded full-scenario deployment capabilities:**
  - High-performance inference supports one-click installation, Windows systems, and 220+ models, with the core library ultra-infer open-sourced;
  - Serving deployment added a highly stable solution, supporting dynamic configuration optimization.

- **Enhanced system compatibility:** adapted to Windows training/inference, fully supporting Python 3.11/3.12.

🔥🔥 **11.15, 2024**, PaddleX 3.0 Beta2 open source version is officially released, PaddleX 3.0 Beta2 is fully compatible with the PaddlePaddle 3.0b2 version. <b>This update introduces new pipelines for general image recognition, face recognition, vehicle attribute recognition, and pedestrian attribute recognition. We have also developed 42 new models to fully support the Ascend 910B, with extensive documentation available on [GitHub Pages](https://paddlepaddle.github.io/PaddleX/latest/en/index.html).</b>

🔥🔥 **9.30, 2024**, PaddleX 3.0 Beta1 open source version is officially released, providing **more than 200 models** that can be called with a simple Python API; achieve model full-process development based on unified commands, and open source the basic capabilities of the **PP-ChatOCRv3** pipeline; support **more than 100 models for high-performance inference and serving** (iterating continuously), **more than 7 key visual models for edge-deployment**; **more than 70 models have been adapted for the full development process of Ascend 910B**, **more than 15 models have been adapted for the full development process of Kunlun chips and Cambricon**

🔥 **6.27, 2024**, PaddleX 3.0 Beta open source version is officially released, supporting the use of various mainstream hardware for pipeline and model development in a low-code manner on the local side.

🔥 **3.25, 2024**, PaddleX 3.0 cloud release, supporting the creation of pipelines in the AI Studio  Community in a zero-code manner.

## 🔠 Explanation of Pipeline
PaddleX is dedicated to achieving pipeline-level model training, inference, and deployment. A pipeline refers to a series of predefined development processes for specific AI tasks, which includes a combination of single models (single-function modules) capable of independently completing a certain type of task.

## 📊 What can PaddleX do？


All pipelines of PaddleX support **online experience** on [AI Studio]((https://aistudio.baidu.com/overview)) and local **fast inference**. You can quickly experience the effects of each pre-trained pipeline. If you are satisfied with the effects of the pre-trained pipeline, you can directly perform [high-performance inference](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/high_performance_inference.html) / [serving](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/serving.html) / [edge deployment](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/edge_deploy.html) on the pipeline. If not satisfied, you can also **Custom Development** to improve the pipeline effect. For the complete pipeline development process, please refer to the [PaddleX pipeline Development Tool Local Use Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/pipeline_develop_guide.html).

In addition, PaddleX provides developers with a full-process efficient model training and deployment tool based on a [cloud-based GUI](https://aistudio.baidu.com/pipeline/mine). Developers **do not need code development**, just need to prepare a dataset that meets the pipeline requirements to **quickly start model training**. For details, please refer to the tutorial ["Developing Industrial-level AI Models with Zero Barrier"](https://aistudio.baidu.com/practical/introduce/546656605663301).

<table>
    <tr>
        <th>Pipeline</th>
        <th>Online Experience</th>
        <th>Local Inference</th>
        <th>High-Performance Inference</th>
        <th>Serving</th>
        <th>Edge Deployment</th>
        <th>Custom Development</th>
        <th><a href="https://aistudio.baidu.com/pipeline/mine">Zero-Code Development On AI Studio</a></td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/OCR.html">OCR</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/91660/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.html">PP-ChatOCRv3</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/182491/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition.html">Table Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/91661?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/object_detection.html">Object Detection</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/70230/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.html">Instance Segmentation</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100063/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_classification.html">Image Classification</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100061/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.html">Semantic Segmentation</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/100062/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.html">Time Series Forecasting</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105706/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.html">Time Series Anomaly Detection</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105708/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.html">Time Series Classification</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/105707/webUI?source=appMineRecent">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
        <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/small_object_detection.html">Small Object Detection</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387975/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
        <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.html">Multi-label Image Classification</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387974/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/pedestrian_attribute_recognition.html">Pedestrian Attribute Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387978/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/vehicle_attribute_recognition.html">Vehicle Attribute Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387979/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/formula_recognition.html">Formula Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387976/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/seal_recognition.html">Seal Recognition</a></td>
        <td><a href="https://aistudio.baidu.com/community/app/387977/webUI?source=appCenter">Link</a></td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.html">Image Anomaly Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/human_keypoint_detection.html">Human Keypoint Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_detection.html">Open Vocabulary Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_segmentation.html">Open Vocabulary Segmentation</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/rotated_object_detection.html">Rotated Object Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/3d_bev_detection.html">3D Bev Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition_v2.html">Table Recognition v2</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/layout_parsing.html">Layout Parsing</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/layout_parsing_v2.html">Layout Parsing v2</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/doc_preprocessor.html">Document Image Preprocessing</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/general_image_recognition.html">Image Recognition</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/face_recognition.html">Face Recognition</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>✅</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/speech_pipelines/multilingual_speech_recognition.html">Multilingual Speech Recognition</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>🚧</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/video_pipelines/video_classification.html">Video Classification</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>
    <tr>
        <td><a href="https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/video_pipelines/video_detection.html">Video Detection</a></td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
        <td>✅</td>
        <td>🚧</td>
    </tr>

</table>

> ❗Note: The above capabilities are implemented based on GPU/CPU. PaddleX can also perform local inference and custom development on mainstream hardware such as Kunlunxin, Ascend, Cambricon, and Haiguang. The table below details the support status of the pipelines. For specific supported model lists, please refer to the [Model List (Kunlunxin XPU)](https://paddlepaddle.github.io/PaddleX/latest/en/support_list/model_list_xpu.html)/[Model List (Ascend NPU)](https://paddlepaddle.github.io/PaddleX/latest/en/support_list/model_list_npu.html)/[Model List (Cambricon MLU)](https://paddlepaddle.github.io/PaddleX/latest/en/support_list/model_list_mlu.html)/[Model List (Haiguang DCU)](https://paddlepaddle.github.io/PaddleX/latest/en/support_list/model_list_dcu.html). We are continuously adapting more models and promoting the implementation of high-performance and serving on mainstream hardware.

🔥🔥 **Support for Domestic Hardware Capabilities**

<table>
  <tr>
    <th>Pipeline</th>
    <th>Ascend 910B</th>
    <th>Kunlunxin R200/R300</th>
    <th>Cambricon MLU370X8</th>
    <th>Haiguang Z100</th>
  </tr>
  <tr>
    <td>OCR</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Table Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Object Detection</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Instance Segmentation</td>
    <td>✅</td>
    <td>🚧</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Image Classification</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Semantic Segmentation</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Time Series Forecasting</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Time Series Anomaly Detection</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Time Series Classification</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Multi-label Image Classification</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Pedestrian Attribute Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Vehicle Attribute Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Image Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Seal Recognition</td>
    <td>✅</td>
    <td>🚧</td>
    <td>🚧</td>
    <td>🚧</td>
  </tr>
  <tr>
    <td>Image Anomaly Detection</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Face Recognition</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
</table>


## ⏭️ Quick Start

### 🛠️ Installation

> ❗Before installing PaddleX, please ensure you have a basic **Python runtime environment** (Note: Currently supports running under Python 3.8 to Python 3.12, with more Python versions under adaptation). The PaddlePaddle version required by PaddleX

* **Installing PaddlePaddle**

```bash
# CPU
python -m pip install paddlepaddle==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# gpu，requires GPU driver version ≥450.80.02 (Linux) or ≥452.39 (Windows)
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# gpu，requires GPU driver version ≥545.23.06 (Linux) or ≥545.84 (Windows)
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
```
> ❗No need to focus on the CUDA version on the physical machine, only the GPU driver version needs attention. For more information on PaddlePaddle Wheel versions, please refer to the [PaddlePaddle Official Website](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation./docs/en/install/pip/linux-pip.html).

* **Installing PaddleX**

```bash
pip install https://paddle-model-ecology.bj.bcebos.com/paddlex/whl/paddlex-3.0.0rc0-py3-none-any.whl
```

> ❗For more installation methods, refer to the [PaddleX Installation Guide](https://paddlepaddle.github.io/PaddleX/latest/en/installation/installation.html).


### 💻 CLI Usage

One command can quickly experience the pipeline effect, the unified CLI format is:

```bash
paddlex --pipeline [Pipeline Name] --input [Input Image] --device [Running Device]
```

Each Pipeline in PaddleX corresponds to specific parameters, which you can view in the respective Pipeline documentation for detailed explanations. Each Pipeline requires specifying three necessary parameters:
* `pipeline`: The name of the Pipeline or the configuration file of the Pipeline
* `input`: The local path, directory, or URL of the input file (e.g., an image) to be processed
* `device`: The hardware device and its index to use (e.g., `gpu:0` indicates using the 0th GPU), or you can choose to use NPU (`npu:0`), XPU (`xpu:0`), CPU (`cpu`), etc.

For example, using the  OCR pipeline:
```bash
paddlex --pipeline OCR \
        --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png \
        --use_doc_orientation_classify False \
        --use_doc_unwarping False \
        --use_textline_orientation False \
        --save_path ./output \
        --device gpu:0
```
<details>
  <summary><b>👉 Click to view the running result</b></summary>

```bash
{'res': {'input_path': 'general_ocr_002.png', 'page_index': None, 'model_settings': {'use_doc_preprocessor': False, 'use_textline_orientation': False}, 'doc_preprocessor_res': {'input_path': None, 'model_settings': {'use_doc_orientation_classify': True, 'use_doc_unwarping': False}, 'angle': 0},'dt_polys': [array([[ 3, 10],
       [82, 10],
       [82, 33],
       [ 3, 33]], dtype=int16), ...], 'text_det_params': {'limit_side_len': 960, 'limit_type': 'max', 'thresh': 0.3, 'box_thresh': 0.6, 'unclip_ratio': 2.0}, 'text_type': 'general', 'textline_orientation_angles': [-1, ...], 'text_rec_score_thresh': 0.0, 'rec_texts': ['www.99*', ...], 'rec_scores': [0.8980069160461426,  ...], 'rec_polys': [array([[ 3, 10],
       [82, 10],
       [82, 33],
       [ 3, 33]], dtype=int16), ...], 'rec_boxes': array([[  3,  10,  82,  33], ...], dtype=int16)}}
```

The visualization result is as follows:

![alt text](https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/boardingpass.png)

</details>

To use the command line for other pipelines, simply adjust the `pipeline` parameter to the name of the corresponding pipeline and modify the parameters accordingly. Below are the commands for each pipeline:

<details>
  <summary><b>👉 More CLI usage for pipelines</b></summary>

| Pipeline Name                | Command                                                                                                                                                                                    |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General Image Classification       | `paddlex --pipeline image_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg --device gpu:0 --save_path ./output/`                    |
| General Object Detection         | `paddlex --pipeline object_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_object_detection_002.png --threshold 0.5 --save_path ./output/ --device gpu:0`                            |
| General Instance Segmentation    | `paddlex --pipeline instance_segmentation --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_instance_segmentation_004.png --threshold 0.5 --save_path ./output --device gpu:0`                  |
| General Semantic Segmentation    | `paddlex --pipeline semantic_segmentation --input https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/application/semantic_segmentation/makassaridn-road_demo.png --target_size -1 --save_path ./output --device gpu:0` |
| Image Multi-label Classification | `paddlex --pipeline image_multilabel_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg --save_path ./output --device gpu:0`        |
| Small Object Detection           | `paddlex --pipeline small_object_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/small_object_detection.jpg --threshold 0.5 --save_path ./output --device gpu:0`                            |
| Image Anomaly Detection          | `paddlex --pipeline anomaly_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/uad_grid.png --save_path ./output --device gpu:0`                                              |
| Pedestrian Attribute Recognition | `paddlex --pipeline pedestrian_attribute_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/pedestrian_attribute_002.jpg --save_path ./output/ --device gpu:0`                                              |
| Vehicle Attribute Recognition    | `paddlex --pipeline vehicle_attribute_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/vehicle_attribute_002.jpg --save_path ./output/ --device gpu:0`                                              |
| 3D Multi-modal Fusion Detection  | `paddlex --pipeline 3d_bev_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/det_3d/demo_det_3d/nuscenes_demo_infer.tar --device gpu:0 --save_path ./output/`                    |
| Human Keypoint Detection         | `paddlex --pipeline human_keypoint_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/keypoint_detection_001.jpg --det_threshold 0.5 --save_path ./output/ --device gpu:0`                    |
| Open Vocabulary Detection        | `paddlex --pipeline open_vocabulary_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/open_vocabulary_detection.jpg --prompt "bus . walking man . rearview mirror ." --thresholds "{'text_threshold': 0.25, 'box_threshold': 0.3}" --save_path ./output --device gpu:0`                    |
| Open Vocabulary Segmentation     | `paddlex --pipeline open_vocabulary_segmentation --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/open_vocabulary_segmentation.jpg --prompt_type box --prompt "[[112.9,118.4,513.8,382.1],[4.6,263.6,92.2,336.6],[592.4,260.9,607.2,294.2]]" --save_path ./output --device gpu:0`                    |
| Rotated Object Detection         | `paddlex --pipeline rotated_object_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/rotated_object_detection_001.png --threshold 0.5 --save_path ./output --device gpu:0`                    |
| General OCR                      | `paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False --save_path ./output --device gpu:0`                                      |
| Document Image Preprocessor      | `paddlex --pipeline doc_preprocessor --input https://paddle-model-ecology.bj.bcebos.com/paddlex/demo_image/doc_test_rotated.jpg --use_doc_orientation_classify True --use_doc_unwarping True --save_path ./output --device gpu:0`                                                      |
| General Table Recognition        | `paddlex --pipeline table_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/table_recognition.jpg --save_path ./output --device gpu:0`                                      |
| General Table Recognition v2     | `paddlex --pipeline table_recognition_v2 --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/table_recognition.jpg --save_path ./output --device gpu:0`                                      |
| General Layout Parsing           | `paddlex --pipeline layout_parsing --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/demo_paper.png --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False --save_path ./output --device gpu:0`                      |
| General Layout Parsing v2        | `paddlex --pipeline layout_parsing_v2 --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/layout_parsing_v2_demo.png --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False --save_path ./output --device gpu:0`                      |
| Formula Recognition              | `paddlex --pipeline formula_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/demo_image/general_formula_recognition.png --use_layout_detection True --use_doc_orientation_classify False --use_doc_unwarping False --layout_threshold 0.5 --layout_nms True --layout_unclip_ratio  1.0 --layout_merge_bboxes_mode large --save_path ./output --device gpu:0`                                      |
| Seal Text Recognition            | `paddlex --pipeline seal_recognition --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png --use_doc_orientation_classify False --use_doc_unwarping False --device gpu:0 --save_path ./output`                                      |
| Time Series Forecasting       | `paddlex --pipeline ts_forecast --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_fc.csv --device gpu:0 --save_path ./output`                                                                   |
| Time Series Anomaly Detection | `paddlex --pipeline ts_anomaly_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv --device gpu:0 --save_path ./output`                                                                    |
| Time Series Classification    | `paddlex --pipeline ts_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_cls.csv --device gpu:0 --save_path ./output`                                                                 |
| Multilingual Speech Recognition   | `paddlex --pipeline multilingual_speech_recognition --input https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav --save_path ./output --device gpu:0`                                      |
| General Video Classification   | `paddlex --pipeline video_classification --input https://paddle-model-ecology.bj.bcebos.com/paddlex/videos/demo_video/general_video_classification_001.mp4 --topk 5 --save_path ./output --device gpu:0`                     |
| General Video Detection       | `paddlex --pipeline video_detection --input https://paddle-model-ecology.bj.bcebos.com/paddlex/videos/demo_video/HorseRiding.avi --device gpu:0 --save_path ./output`                     |

</details>

### 📝 Python Script Usage

A few lines of code can complete the quick inference of the pipeline, the unified Python script format is as follows:
```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline=[Pipeline Name])
output = pipeline.predict([Input Image Name])
for res in output:
    res.print()
    res.save_to_img("./output/")
    res.save_to_json("./output/")
```
The following steps are executed:

* `create_pipeline()` instantiates the pipeline object
* Passes the image and calls the `predict()` method of the pipeline object for inference prediction
* Processes the prediction results

To use the Python script for other pipelines, simply adjust the `pipeline` parameter in the `create_pipeline()` method to the name of the corresponding pipeline and modify the parameters accordingly. Below are the parameter names and detailed usage explanations for each pipeline:

<details>
  <summary>👉 More Python script usage for pipelines</summary>

| pipeline Name           | Corresponding Parameter               | Detailed Explanation                                                                                                      |
|-------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| PP-ChatOCRv4-doc | `PP-ChatOCRv4-doc` | [PP-ChatOCRv4-doc Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction_v4.html) |
| PP-ChatOCRv3-doc   | `PP-ChatOCRv3-doc` | [PP-ChatOCRv3-doc Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction_v3.html) |
|  Image Classification       | `image_classification` | [ Image Classification Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_classification.html) |
|  Object Detection       | `object_detection` | [ Object Detection Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/object_detection.html) |
|  Instance Segmentation       | `instance_segmentation` | [ Instance Segmentation Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.html) |
|  Semantic Segmentation       | `semantic_segmentation` | [ Semantic Segmentation Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.html) |
|  Image Multi-Label Classification | `multilabel_classification` | [ Image Multi-Label Classification Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.html) |
| Small Object Detection         | `small_object_detection` | [Small Object Detection Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/small_object_detection.html) |
| Image Anomaly Detection       | `image_classification` | [Image Anomaly Detection Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.html) |
| Image Recognition       | `PP-ShiTuV2`                | [Image Recognition Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/general_image_recognition.html)                              |
| Face Recognition       | `face_recognition`                | [Face Recognition Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/face_recognition.html)                              |
| Pedestrian Attribute Recognition       | `pedestrian_attribute`                | [Pedestrian Attribute Recognition Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/pedestrian_attribute_recognition.html)                              |
|Vehicle Attribute Recognition       | `vehicle_attribute`                | [Vehicle Attribute Recognition Pipeline Python Script Usage Instructions](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/vehicle_attribute_recognition.html)                              |
| 3D Multi-modal Fusion Detection | `3d_bev_detection` | [Instructions for Using the 3D Multi-modal Fusion Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/cv_pipelines/3d_bev_detection.html#222-python-script-integration) |
| Human Keypoint Detection | `human_keypoint_detection` | [Instructions for Using the Human Keypoint Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/cv_pipelines/human_keypoint_detection.html#222-python-script-integration) |
| Open Vocabulary Detection | `open_vocabulary_detection` | [Instructions for Using the Open Vocabulary Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_detection.html#212-python-script-integration) |
| Open Vocabulary Segmentation | `open_vocabulary_segmentation` | [Instructions for Using the Open Vocabulary Segmentation Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_segmentation.html#212-python-script-integration) |
| Rotated Object Detection | `rotated_object_detection` | [Instructions for Using the Rotated Object Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/cv_pipelines/rotated_object_detection.html#212-python-script-integration) |
| OCR | `OCR` | [Instructions for Using the General OCR Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/OCR.html#222-python-script-integration) |
| Document Image Preprocessing | `doc_preprocessor` | [Instructions for Using the Document Image Preprocessing Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/doc_preprocessor.html#212-python-script-integration) |
| General Table Recognition | `table_recognition` | [Instructions for Using the General Table Recognition Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/table_recognition.html#22-python-script-integration) |
| General Table Recognition v2 | `table_recognition_v2` | [Instructions for Using the General Table Recognition v2 Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/table_recognition_v2.html#22-python-script-integration) |
| General Layout Parsing | `layout_parsing` | [Instructions for Using the General Layout Parsing Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/layout_parsing.html#22-python-script-integration) |
| General Layout Parsing v2 | `layout_parsing_v2` | [Instructions for Using the General Layout Parsing v2 Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/layout_parsing_v2.html#22-python-script-integration) |
| Formula Recognition | `formula_recognition` | [Instructions for Using the Formula Recognition Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/formula_recognition.html#22-python-script-integration) |
| Seal Text Recognition | `seal_recognition` | [Instructions for Using the Seal Text Recognition Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/ocr_pipelines/seal_recognition.html#22-python-script-integration) |
| Time Series Forecasting | `ts_forecast` | [Instructions for Using the Time Series Forecasting Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.html#222-python-script-integration) |
| Time Series Anomaly Detection | `ts_anomaly_detection` | [Instructions for Using the Time Series Anomaly Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.html#222-python-script-integration) |
| Time Series Classification | `ts_classification` | [Instructions for Using the Time Series Classification Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.html#222-python-script-integration) |
| Multilingual Speech Recognition | `multilingual_speech_recognition` | [Instructions for Using the Multilingual Speech Recognition Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/multilingual_speech_recognition.html#212-python-script-integration) |
| General Video Classification | `video_classification` | [Instructions for Using the General Video Classification Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/video_classification.html#22-python-script-integration) |
| General Video Detection | `video_detection` | [Instructions for Using the General Video Detection Pipeline Python Script](https://paddlepaddle.github.io/PaddleX/latest/pipeline_usage/tutorials/time_series_pipelines/video_detection.html#212-python-script-integration) |
</details>

## 📖 Documentation
<details>
  <summary> <b> ⬇️ Installation </b></summary>

  * [📦 PaddlePaddle Installation](https://paddlepaddle.github.io/PaddleX/latest/en/installation/paddlepaddle_install.html)
  * [📦 PaddleX Installation](https://paddlepaddle.github.io/PaddleX/latest/en/installation/installation.html)

</details>

<details open>
<summary> <b> 🔥 Pipeline Usage </b></summary>

* [📑 PaddleX Pipeline Usage Overview](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/pipeline_develop_guide.html)

* <details open>
    <summary> <b> 📝 Information Extracion</b></summary>

   * [📄 PP-ChatOCRv3 Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/information_extraction_pipelines/document_scene_information_extraction.html)
  </details>

* <details open>
    <summary> <b> 🔍 OCR </b></summary>

    * [📜 OCR Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/OCR.html)
    * [📊 Table Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition.html)
    * [🗂️ Table Recognition v2 Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/table_recognition_v2.html)
    * [📄 Layout Parsing Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/layout_parsing.html)
    * [🗞️ Layout Parsing v2 Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/layout_parsing_v2.html)
    * [📐 Formula Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/formula_recognition.html)
    * [📝 Seal Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/seal_recognition.html)
    * [🖌️ Document Image Preprocessing](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/ocr_pipelines/doc_preprocessor.html)
  </details>

* <details open>
    <summary> <b> 🎥 Computer Vision </b></summary>

   * [🖼️ Image Classification Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_classification.html)
   * [🎯 Object Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/object_detection.html)
   * [📋 Instance Segmentation Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/instance_segmentation.html)
   * [🗣️ Semantic Segmentation Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/semantic_segmentation.html)
   * [🏷️ Multi-label Image Classification Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_multi_label_classification.html)
   * [🔍 Small Object Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/small_object_detection.html)
   * [🖼️ Image Anomaly Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/image_anomaly_detection.html)
   * [🔍 Human Keypoint Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/human_keypoint_detection.html)
   * [📚 Open Vocabulary Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_detection.html)
   * [🎨 Open Vocabulary Segmentation Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/open_vocabulary_segmentation.html)
   * [🔄 Rotated Object Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/rotated_object_detection.html)
   * [🌐 3D Bev Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/3d_bev_detection.html)
   * [🖼️ Image Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/general_image_recognition.html)
   * [🆔 Face Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/face_recognition.html)
   * [🚗 Vehicle Attribute Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/vehicle_attribute.html)
   * [🚶‍♀️ Pedestrian Attribute Recognition Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/cv_pipelines/pedestrian_attribute.html)
  </details>

* <details open>
    <summary> <b> ⏱️ Time Series Analysis</b> </summary>

   * [📈 Time Series Forecasting Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_forecasting.html)
   * [📉 Time Series Anomaly Detection Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_anomaly_detection.html)
   * [🕒 Time Series Classification Pipeline Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/time_series_pipelines/time_series_classification.html)
  </details>

* <details open>
    <summary> <b> 🎤 Speech Recognition</b> </summary>

    * [🌐 Multilingual Speech Recognition Pipeline Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/speech_pipelines/multilingual_speech_recognition.html)

* <details open>
    <summary> <b> 🎥 Video Recognition</b> </summary>

    * [📈 General Video Classification Pipeline Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/video_pipelines/video_classification.html)
    * [🔍 General Video Detection Pipeline Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/tutorials/video_pipelines/video_detection.html)

* <details open>
    <summary> <b>🔧 Related Instructions</b> </summary>

   * [🖥️ PaddleX pipeline Command Line Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/instructions/pipeline_CLI_usage.html)
   * [📝 PaddleX pipeline Python Script Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_usage/instructions/pipeline_python_API.html)
  </details>

</details>

<details open>
<summary> <b> ⚙️ Module Usage </b></summary>

* <details open>
  <summary> <b> 🔍 OCR </b></summary>

  * [📝 Text Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/text_detection.html)
  * [🔖 Seal Text Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/seal_text_detection.html)
  * [🔠 Text Recognition Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/text_recognition.html)
  * [🗺️ Layout Parsing Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/layout_detection.html)
  * [📊 Table Structure Recognition Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/table_structure_recognition.html)
  * [📄 Document Image Orientation Classification Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/doc_img_orientation_classification.html)
  * [🔧 Document Image Unwarp Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/text_image_unwarping.html)
  * [📐 Formula Recognition Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/formula_recognition.html)
  * [📊 Table Cell Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/table_cells_detection.html)
  * [📈 Table Classification Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/table_classification.html)
  * [📝 Text Line Orientation Classification Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/textline_orientation_classification.html)
  </details>

* <details open>
  <summary> <b> 🖼️ Image Classification </b></summary>

  * [📂 Image Classification Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/image_classification.html)
  * [🏷️ Multi-label Image Classification Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/image_multilabel_classification.html)

  * [👤 Pedestrian Attribute Recognition Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/pedestrian_attribute_recognition.html)
  * [🚗 Vehicle Attribute Recognition Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/vehicle_attribute_recognition.html)

  </details>

* <details open>
  <summary> <b> 🏞️ Image Features </b></summary>

    * [🔗 Image Feature Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/image_feature.html)
    * [😁 Face_Feature Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/face_feature.html)
  </details>

* <details open>
  <summary> <b> 🎯 Object Detection </b></summary>

  * [🎯 Object Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/object_detection.html)
  * [📏 Small Object Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/small_object_detection.html)
  * [🧑‍🤝‍🧑 Face Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/face_detection.html)
  * [🔍 Mainbody Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/mainbody_detection.html)
  * [🚶 Pedestrian Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/human_detection.html)
  * [🚗 Vehicle Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/vehicle_detection.html)
  * [🔄 Rotated Object Detection Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/rotated_object_detection.html)

  </details>

* <details open>
  <summary> <b> 🌐 Open-Vocabulary Object Detection </b></summary>

  * [🌐 Open-Vocabulary Object Detection Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/open_vocabulary_detection.html)
</details>

* <details open>
  <summary> <b> 🎯 Keypoint Detection </b></summary>

  * [🚶‍♂️ Human Keypoint Detection Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/human_keypoint_detection.html)
   </details>




* <details open>
  <summary> <b> 🖼️ Image Segmentation </b></summary>

  * [🗺️ Semantic Segmentation Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/semantic_segmentation.html)
  * [🔍 Instance Segmentation Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/instance_segmentation.html)
  * [🚨 Image Anomaly Detection Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/anomaly_detection.html)
  </details>

* <details open>
  <summary> <b> 🌐 Open-Vocabulary Segmentation </b></summary>

  * [🌐 Open-Vocabulary Segmentation Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/open_vocabulary_segmentation.html)
  </details>

* <details open>
  <summary> <b> ⏱️ Time Series Analysis </b></summary>

  * [📈 Time Series Forecasting Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/time_series_modules/time_series_forecasting.html)
  * [🚨 Time Series Anomaly Detection Module Tutorial](./docs/module_usage/tutorials/time_series_modules/time_series_anomaly_detection.md)
  * [🕒 Time Series Classification Module Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/time_series_modules/time_series_classification.html)
  </details>

* <details open>
  <summary> <b> 📦 3D  </b></summary>

  * [📦 3D Multimodal Fusion Detection Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/cv_modules/3d_bev_detection.html)

* <details open>
  <summary> <b> 🎤 Speech Recognition </b></summary>

  * [🌐 Multilingual Speech Recognition Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/speech_modules/multilingual_speech_recognition.html)

* <details open>
  <summary> <b> 🎥 Video Recognition </b></summary>

  * [📈 Video Classification Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/module_usage/tutorials/video_modules/video_classification.html)
  * [🔍 Video Detection Module Usage Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/video_modules/video_detection.html)

* <details open>
  <summary> <b> 📄 Related Instructions </b></summary>

  * [📝 PaddleX Single Model Python Script Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/instructions/model_python_API.html)
  * [📝 PaddleX General Model Configuration File Parameter Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/instructions/config_parameters_common.html)
  * [📝 PaddleX Time Series Task Model Configuration File Parameter Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/instructions/config_parameters_time_series.html)
  * [📝 PaddleX 3D Task Model Configuration File Parameter Instruction](https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/instructions/config_parameters_3d.html)
  </details>

</details>

<details open>
  <summary> <b> 🏗️ Pipeline Deployment </b></summary>

  * [🚀 PaddleX High-Performance Inference Guide](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/high_performance_inference.html)
  * [🖥️ PaddleX Serving Guide](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/serving.html)
  * [📱 PaddleX Edge Deployment Guide](https://paddlepaddle.github.io/PaddleX/latest/en/pipeline_deploy/edge_deploy.html)

</details>
<details open>
  <summary> <b> 🖥️ Multi-Hardware Usage </b></summary>

  * [⚙️ Multi-Hardware Usage Guide](https://paddlepaddle.github.io/PaddleX/latest/en/other_devices_support/multi_devices_use_guide.html)
  * [⚙️ DCU Paddle Installation](https://paddlepaddle.github.io/PaddleX/latest/en/other_devices_support/paddlepaddle_install_DCU.html)
  * [⚙️ MLU Paddle Installation](https://paddlepaddle.github.io/PaddleX/latest/en/other_devices_support/paddlepaddle_install_MLU.html)
  * [⚙️ NPU Paddle Installation](https://paddlepaddle.github.io/PaddleX/latest/en/other_devices_support/paddlepaddle_install_NPU.html)
  * [⚙️ XPU Paddle Installation](https://paddlepaddle.github.io/PaddleX/latest/en/other_devices_support/paddlepaddle_install_XPU.html)

</details>

<details>
  <summary> <b> 📝 Tutorials & Examples </b></summary>

* [📑 PP-ChatOCRv3 Model Line —— Paper Document Information Extract Tutorial](./docs/practical_tutorials/document_scene_information_extraction(layout_detection)_tutorial_en.md)
* [📑 PP-ChatOCRv3 Model Line —— Seal Information Extract Tutorial](./docs/practical_tutorials/document_scene_information_extraction(seal_recognition)_tutorial_en.md)
* [🖼️ General Image Classification Model Line —— Garbage Classification Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/image_classification_garbage_tutorial.html)
* [🧩 General Instance Segmentation Model Line —— Remote Sensing Image Instance Segmentation Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/instance_segmentation_remote_sensing_tutorial.html)
* [👥 General Object Detection Model Line —— Pedestrian Fall Detection Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/object_detection_fall_tutorial.html)
* [👗 General Object Detection Model Line —— Fashion Element Detection Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/object_detection_fashion_pedia_tutorial.html)
* [🚗 General OCR Model Line —— License Plate Recognition Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/ocr_det_license_tutorial.html)
* [✍️ General OCR Model Line —— Handwritten Chinese Character Recognition Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/ocr_rec_chinese_tutorial.html)
* [🗣️ General Semantic Segmentation Model Line —— Road Line Segmentation Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/semantic_segmentation_road_tutorial.html)
* [🛠️ Time Series Anomaly Detection Model Line —— Equipment Anomaly Detection Application Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/ts_anomaly_detection.html)
* [🎢 Time Series Classification Model Line —— Heartbeat Monitoring Time Series Data Classification Application Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/ts_classification.html)
* [🔋 Time Series Forecasting Model Line —— Long-term Electricity Consumption Forecasting Application Tutorial](https://paddlepaddle.github.io/PaddleX/latest/en/practical_tutorials/ts_forecast.html)

  </details>




## 🤔 FAQ

For answers to some common questions about our project, please refer to the [FAQ](https://paddlepaddle.github.io/PaddleX/latest/en/FAQ.html). If your question has not been answered, please feel free to raise it in [Issues](https://github.com/PaddlePaddle/PaddleX/issues).

## 💬 Discussion

We warmly welcome and encourage community members to raise questions, share ideas, and feedback in the [Discussions](https://github.com/PaddlePaddle/PaddleX/discussions) section. Whether you want to report a bug, discuss a feature request, seek help, or just want to keep up with the latest project news, this is a great platform.

## 📄 License

The release of this project is licensed under the [Apache 2.0 license](https://github.com/PaddlePaddle/PaddleX/blob/release/3.0-beta/LICENSE).
