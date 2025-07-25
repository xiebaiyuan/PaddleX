#!/bin/bash

# input
CONTAINER_NAME="${CONTAINER_NAME:-build}"
WITH_GPU="${WITH_GPU:-ON}"
ENABLE_BENCHMARK="${ENABLE_BENCHMARK:-OFF}"
DEBUG="${DEBUG:-OFF}"
ENABLE_ORT_BACKEND="${ENABLE_ORT_BACKEND:-ON}"
ENABLE_OPENVINO_BACKEND="${ENABLE_OPENVINO_BACKEND:-ON}"
ENABLE_TRT_BACKEND="${ENABLE_TRT_BACKEND:-ON}"
TRT_DIRECTORY="${TRT_DIRECTORY:-Default}"

if [ "$WITH_GPU" = "OFF" ]; then
    ENABLE_TRT_BACKEND="OFF"
fi

DOCKER_IMAGE="ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle_manylinux_devel:cuda11.8-cudnn8.6-trt8.5-gcc8.2"

# Set variables
CMAKE_CXX_COMPILER="/usr/local/gcc-8.2/bin/g++"

# Get the current script directory and compute the directory to mount
SCRIPT_DIR="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"
ULTRAINFER_DIR="$(realpath "$SCRIPT_DIR/../../../")"

# Set the Docker startup command
if [ "$WITH_GPU" = "ON" ]; then
    DOCKER_CMD=$(cat << EOF
docker run --gpus all -it --name="${CONTAINER_NAME}" --shm-size=128g --net=host \
-v "${ULTRAINFER_DIR}":/workspace \
-e CMAKE_CXX_COMPILER="${CMAKE_CXX_COMPILER}" \
-e "http_proxy=${http_proxy}" \
-e "https_proxy=${https_proxy}" \
"${DOCKER_IMAGE}" /bin/bash -c "
ldconfig && \
cd /workspace && \
./ultra-infer/scripts/linux/_build_cpp.sh --with-gpu "${WITH_GPU}" --enable-benchmark "${ENABLE_BENCHMARK}" --enable-ort-backend "${ENABLE_ORT_BACKEND}" --enable-openvino-backend "${ENABLE_OPENVINO_BACKEND}" --enable-trt-backend "${ENABLE_TRT_BACKEND}" --trt-directory "${TRT_DIRECTORY}" && \
tail -f /dev/null"
EOF
)
else
    DOCKER_CMD=$(cat << EOF
docker run -it --name="${CONTAINER_NAME}" --shm-size=128g --net=host \
-v "${ULTRAINFER_DIR}":/workspace \
-e CMAKE_CXX_COMPILER="${CMAKE_CXX_COMPILER}" \
-e "http_proxy=${http_proxy}" \
-e "https_proxy=${https_proxy}" \
"${DOCKER_IMAGE}" /bin/bash -c "
cd /workspace && \
./ultra-infer/scripts/linux/_build_cpp.sh --with-gpu "${WITH_GPU}" --enable-benchmark "${ENABLE_BENCHMARK}" --enable-ort-backend "${ENABLE_ORT_BACKEND}" --enable-openvino-backend "${ENABLE_OPENVINO_BACKEND}" --enable-trt-backend "${ENABLE_TRT_BACKEND}" --trt-directory "${TRT_DIRECTORY}" && \
tail -f /dev/null"
EOF
)
fi

# If in debug mode, replace --rm with -it and keep the container running
if [ "$DEBUG" = "OFF" ]; then
    DOCKER_CMD="${DOCKER_CMD/-it/--rm}"
    DOCKER_CMD="${DOCKER_CMD/ && tail -f \/dev\/null/}"
fi

# Check if a Docker container with the same name already exists
if docker ps -a --format '{{.Names}}' | grep -Eq "^${CONTAINER_NAME}\$"; then
    echo "Error: A Docker container with the name '${CONTAINER_NAME}' already exists."
    echo "Please remove the existing container or choose a different container name."
    exit 1
fi

echo "Starting Docker container..."
eval "$DOCKER_CMD"
