#!/bin/bash

python tools/test_cv_ensemble.py \
    --cfg experiments/sun_hpc_001.yaml \
    DATA_DIR /project/scratch/p200249/mruthven/speedplus/sunlamp/images \
    OUTPUT_DIR sunlamp_test \
    DATASET.ROOT ../object_detection/sunlamp_test \
    DATASET.TEST_SET real_test \
    TEST.MODEL_FILE sunlamp_model/PEdataset/hrnet_cms/sun_hpc_001/model_best.pth \
    DATASET.IMAGE_WIDTH 1900 \
    DATASET.IMAGE_HEIGHT 1200 \
    MODEL.NUM_JOINTS 11