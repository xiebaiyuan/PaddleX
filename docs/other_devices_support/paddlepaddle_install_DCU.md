---
comments: true
---

# 海光 DCU 飞桨安装教程

当前 PaddleX 支持海光 Z100 系列芯片。考虑到环境差异性，我们推荐使用<b>飞桨官方发布的海光 DCU 开发镜像</b>，该镜像预装有海光 DCU 基础运行环境库（DTK）。

## 1、docker环境准备
拉取镜像，此镜像仅为开发环境，镜像中不包含预编译的飞桨安装包

```
docker pull ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle-dcu:dtk24.04.1-kylinv10-gcc82
```
参考如下命令启动容器

```
docker run -it --name paddle-dcu-dev -v $(pwd):/work \
  -w=/work --shm-size=128G --network=host --privileged  \
  --device=/dev/kfd --device=/dev/dri --ipc=host --group-add video \
  -u root --ulimit stack=-1:-1 --ulimit memlock=-1:-1 -v /opt/hyhal:/opt/hyhal \
  --cap-add=SYS_PTRACE --security-opt seccomp=unconfined \
  ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle-dcu:dtk24.04.1-kylinv10-gcc82 /bin/bash
```

## 2、安装paddle包
在启动的 docker 容器中，下载并安装飞桨官网发布的 wheel 包。<b>注意</b>：飞桨框架 DCU 版仅支持海光 C86 架构。

```
# 下载并安装 wheel 包
pip install paddlepaddle-dcu==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/dcu/
```
验证安装包 安装完成之后，运行如下命令

```
python -c "import paddle; paddle.utils.run_check()"
```
预期得到如下输出结果

```
PaddlePaddle is installed successfully! Let's start deep learning with PaddlePaddle now.
```
