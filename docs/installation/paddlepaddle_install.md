---
comments: true
---

# 飞桨PaddlePaddle本地安装教程



安装飞桨 PaddlePaddle 时，支持通过 Docker 安装和通过 pip 安装。

## 基于 Docker 安装飞桨
<b>若您通过 Docker 安装</b>，请参考下述命令，使用飞桨官方 Docker 镜像，创建一个名为 `paddlex` 的容器，并将当前工作目录映射到容器内的 `/paddle` 目录：

若您使用的 Docker 版本 >= 19.03，请执行：

```bash
# 对于 cpu 用户:
docker run --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0 /bin/bash

# 对于 gpu 用户:
# GPU 版本，需显卡驱动程序版本 ≥450.80.02（Linux）或 ≥452.39（Windows）
docker run --gpus all --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0-gpu-cuda11.8-cudnn8.6-trt8.5 /bin/bash

# GPU 版本，需显卡驱动程序版本 ≥545.23.06（Linux）或 ≥545.84（Windows）
docker run --gpus all --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0-gpu-cuda12.3-cudnn9.0-trt8.6 /bin/bash
```

* 若您使用的 Docker 版本 <= 19.03 但 >= 17.06，请执行：

<details><summary> 点击展开</summary>

<pre><code class="language-bash"># 对于 cpu 用户:
docker run --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0 /bin/bash

# 对于 gpu 用户:
# CUDA11.8 用户
nvidia-docker run --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0-gpu-cuda11.8-cudnn8.6-trt8.5 /bin/bash

# CUDA12.3 用户
nvidia-docker run --name paddlex -v $PWD:/paddle --shm-size=8G --network=host -it ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.0.0rc0-gpu-cuda12.3-cudnn9.0-trt8.6 /bin/bash
</code></pre></details>

* 若您使用的 Docker 版本 <= 17.06，请升级 Docker 版本。

* 注：更多飞桨官方 docker 镜像请参考[飞桨官网](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/docker/linux-docker.html)。

## 基于 pip 安装飞桨
<b>若您通过 pip 安装</b>，请参考下述命令，用 pip 在当前环境中安装飞桨 PaddlePaddle：

```bash
# cpu
python -m pip install paddlepaddle==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# gpu，该命令仅适用于 CUDA 版本为 11.8 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# gpu，该命令仅适用于 CUDA 版本为 12.3 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
```
> ❗ <b>注</b>：无需关注物理机上的 CUDA 版本，只需关注显卡驱动程序版本。更多飞桨 Wheel 版本请参考[飞桨官网](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html)。

<b>关于其他硬件安装飞桨，请参考</b>[PaddleX多硬件使用指南](../other_devices_support/multi_devices_use_guide.md)<b>。</b>

安装完成后，使用以下命令可以验证 PaddlePaddle 是否安装成功：

```bash
python -c "import paddle; print(paddle.__version__)"
```
如果已安装成功，将输出以下内容：

```bash
3.0.0-rc0
```

> ❗ <b>注</b>：如果在安装的过程中，出现任何问题，欢迎在Paddle仓库中[提Issue](https://github.com/PaddlePaddle/Paddle/issues)。
