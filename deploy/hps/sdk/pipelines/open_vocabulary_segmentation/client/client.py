#!/usr/bin/env python

import argparse
import pprint
import sys
from ast import literal_eval

from paddlex_hps_client import triton_request, utils
from tritonclient import grpc as triton_grpc

OUTPUT_IMAGE_PATH = "out.jpg"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True)
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--prompt_type", type=str, required=True)
    parser.add_argument("--no-visualization", action="store_true")
    parser.add_argument("--url", type=str, default="localhost:8001")

    args = parser.parse_args()

    assert args.prompt_type in (
        "box",
        "point",
    ), "Only support 'box' or 'point' prompt_type"

    client = triton_grpc.InferenceServerClient(args.url)
    input_ = {
        "image": utils.prepare_input_file(args.image),
        "prompt": literal_eval(args.prompt),
        "promptType": args.prompt_type,
    }
    if args.no_visualization:
        input_["visualize"] = False
    output = triton_request(client, "open-vocabulary-segmentation", input_)
    if output["errorCode"] != 0:
        print(f"Error code: {output['errorCode']}", file=sys.stderr)
        print(f"Error message: {output['errorMsg']}", file=sys.stderr)
        sys.exit(1)
    result = output["result"]
    utils.save_output_file(result["image"], OUTPUT_IMAGE_PATH)
    print(f"Output image saved at {OUTPUT_IMAGE_PATH}")
    print("\nMask Infos:")
    pprint.pp(result["maskInfos"])


if __name__ == "__main__":
    main()
