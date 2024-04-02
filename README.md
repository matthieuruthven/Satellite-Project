# Satellite Project

This repository contains instructions and code to estimate the 3D pose of a satellite from 2D images. The 3D pose estimation method, TangoUnchained, was developed by researchers at the [University of Adelaide](https://cs.adelaide.edu.au/~ssl/). TangoUnchained was one of the top performing methods in the European Space Agency Satellite Pose Estimation Competition 2021. More information about the competition and TangoUnchained is available [here](https://www.sciencedirect.com/science/article/pii/S0094576523000048?casa_token=JXkEpfMAhY0AAAAA:77rgqTVSAoatpUrZVM9VNn63ORTN01hxg0CYP2FbXz4X25B7NZNRC4qEpGAtwN3fIet_Mlw26Pvb) and [here](https://kelvins.esa.int/pose-estimation-2021/). This repository contains instructions and code to implement and evaluate the method on Luxembourg's national supercomupter, [MeluXina](https://www.luxprovide.lu/meluxina/).

## Requirements

### Hardware

- Access to [MeluXina](https://www.luxprovide.lu/meluxina/)

### Code

- Code from the [TangoUnchained GitHub repository](https://github.com/mohsij/spacecraft-pose-estimation) 

- Code from this repository

## Instructions

1. Clone the [TangoUnchained GitHub repository](https://github.com/mohsij/spacecraft-pose-estimation). The code will be downloaded into a folder called *spacecraft-pose-estimation*.
```
git clone https://github.com/mohsij/spacecraft-pose-estimation.git
```

2. Clone this repository. The code will be downloaded into a folder called *Satellite-Project*.
```
git clone https://github.com/matthieuruthven/Satellite-Project.git
```

3. Replace the following files in the *spacecraft-pose-estimation* folder with the corresponding files in *Satellite-Project* (NB the files in *Satellite-Project* have the same name and path as the corresponding ones in *spacecraft-pose-estimation*):

    - *landmark_regression/nms/setup_linux.py*
    - *landmark_regression/nms/dataset/lightbox.py*
    - *landmark_regression/nms/dataset/PEdataset.py*
    - *landmark_regression/nms/dataset/sunlamp.py*
    - *landmark_regression/experiments/lit_hpc_001.py*
    - *landmark_regression/experiments/slp_hpc_001.py*

4. Follow the instructions in the [README.md](https://github.com/mohsij/spacecraft-pose-estimation/blob/main/README.md) file of the TangoUnchained GitHub repository to install the software required to run the code.