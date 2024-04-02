#!/bin/bash

python tools/train_da_ms.py \
    --cfg experiments/lit_hpc_001.yaml \
    DATA_DIR /project/scratch/p200249/mruthven/speedplus/synthetic/images \
    DATA_DIR_ADVERSARIAL /project/scratch/p200249/mruthven/speedplus/lightbox/images \
    OUTPUT_DIR lightbox_model \
    DATASET.ROOT ../object_detection/speedplus_dicts \
    DATASET.ROOT_ADVERSARIAL ../object_detection/lightbox_test \
    DATASET.TRAIN_SET synthetic_train \
    DATASET.TRAIN_SET_ADVERSARIAL real_test \
    DATASET.TEST_SET synthetic_validation \
    DATASET.IMAGE_WIDTH 1900 \
    DATASET.IMAGE_HEIGHT 1200 \
    MODEL.NUM_JOINTS 11