#!/bin/bash

python tools/test_cv_ensemble.py \
    --cfg experiments/lit_hpc_001.yaml \
    DATA_DIR /project/scratch/p200249/mruthven/speedplus/lightbox/images \
    OUTPUT_DIR lightbox_test \
    DATASET.ROOT ../object_detection/lightbox_test \
    DATASET.TEST_SET real_test \
    TEST.MODEL_FILE lightbox_model/PEdataset/hrnet_cms/lit_hpc_001/model_best.pth \
    DATASET.IMAGE_WIDTH 1900 \
    DATASET.IMAGE_HEIGHT 1200 \
    MODEL.NUM_JOINTS 11