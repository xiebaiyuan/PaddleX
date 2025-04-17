# 1. More Device Support

The prosperity of the PaddlePaddle ecosystem is inseparable from the contributions of developers and users. We warmly welcome you to provide more device compatibility for PaddleX and greatly appreciate your feedback.

Currently, PaddleX supports Intel/Apple M series CPU, NVIDIA GPUs, XPU, Ascend NPU, Hygon DCU, and MLU. If the device you wish to support is not within the current scope, you can contribute by following the methods below.

## 1.1 Integration Device into PaddlePaddle Backend

The PaddlePaddle deep learning framework provides multiple integration solutions, including operator development and mapping, subgraph and whole graph integration, deep learning compiler backend integration, and open neural network format conversion. Device vendors can flexibly choose based on their chip architecture design and software stack maturity. For specific details, please refer to [PaddlePaddle Custom Device Integration Solutions](https://www.paddlepaddle.org.cn/documentation/docs/en/develop/dev_guides/custom_device_docs/index_en.html).

## 1.2 Support for PaddleCV devkits

Since PaddleX is based on the PaddlePaddle model library, after the device completes the integration into the PaddlePaddle backend, select the corresponding devkit to submit code based on the models already supported by the device to ensure that the relevant devkits are adapted to the corresponding device. Refer to the contribution guides for each devkit:

1. [PaddleClas](https://github.com/PaddlePaddle/PaddleClas/tree/develop)

2. [PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection/tree/develop)

3. [PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg/tree/develop)

4. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/tree/develop)

5. [PaddleTS](https://github.com/PaddlePaddle/PaddleTS/tree/main)

# 2. Updating PaddleX

After completing the device integration into PaddlePaddle and the PaddleCV devkits, you need to update the device recognition-related code and documentation in PaddleX.

## 2.1 Code Related Issues

### 2.1.1 Update Whitelist Settings

Since different AI computing device supports different model lists, PaddleX internally determines whether a specific model is supported on the hardware based on a whitelist. The relevant code is located in `XXX_WHITELIST` in [PaddleX Model Whitelist](../../paddlex/utils/custom_device_list.py). Please configure this list according to actual support conditions.

Additionally, update the `check_supported_device_type` function in [Device Validation](../../paddlex/utils/device.py).

### 2.1.2 Update AI Computing Chip Support List

Update the list of supported AI computing device in PaddleX. The relevant code is located in `SUPPORTED_DEVICE_TYPE` in [PaddleX Hardware Support List](../../paddlex/utils/device.py).

### 2.1.3 Setting Environment Variables

If special environment variables need to be set when using the relevant device, you can modify the device environment setup code. The relevant code is located in the `set_env_for_device_type` function in [PaddleX Environment Variable Settings](../../paddlex/utils/device.py).

### 2.1.4 Update Predictor Option Supported Device List

When creating a Predictor, the PaddleX checks whether the device is supported. The relevant code is located in `SUPPORT_DEVICE` in [PaddleX Predictor Option](../../paddlex/inference/utils/pp_option.py).

### 2.1.5 Update Predictor Creation Logic

PaddleX's inference capability is provided based on the Paddle Inference Predictor. When creating a Predictor, you need to select different device based on device information and create passes. The relevant code is located in the `_create` function in [PaddleX Predictor Creation](../../paddlex/inference/models/common/static_infer.py).

### 2.1.6 High-Performance Inference Support

TODO

## 2.2 Documentation Related Issues

### 2.2.1 Updating the Multi-Devices User Guide

Please update the PaddleX multi-devices user guide and add the newly supported device information to the documentation. Both Chinese and English versions need to be updated. The Chinese version is [PaddleX多硬件使用指南](./multi_devices_use_guide.md), and the English version is [PaddleX Multi-Devices Usage Guide](./multi_devices_use_guide.en.md).

### 2.2.2 Updating the Installation Tutorial

Please provide device-related installation tutorials in both Chinese and English. The Chinese version can refer to [昇腾 NPU 飞桨安装教程](./paddlepaddle_install_NPU.md), and the English version can refer to [Ascend NPU PaddlePaddle Installation Tutorial](./paddlepaddle_install_NPU.en.md).

### 2.2.3 Updating the Model List

Please provide a list of models supported by the device in both Chinese and English. The Chinese version can refer to [PaddleX模型列表（昇腾 NPU）](../support_list/model_list_npu.md), and the English version can refer to [PaddleX Model List (Huawei Ascend NPU)](../support_list/model_list_npu.en.md).

# 3. Submitting a PR

When you complete the device adaptation work, please submit a [Pull Request](https://github.com/PaddlePaddle/PaddleX/pulls) to PaddleX with relevant information. We will validate the model and merge the relevant code after confirmation.

The relevant PR needs to provide information on reproducing model accuracy, including at least the following:

* The software versions used to validate model accuracy, including but not limited to:

  * Paddle version

  * PaddleCustomDevice version (if any)

  * The branch of PaddleX or the corresponding devkit

* The machine environment used to validate model accuracy, including but not limited to:

  * Chip model

  * Operating system version

  * Device driver version

  * Operator library version, etc.
