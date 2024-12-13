# Realtime Sign Language Recognition for SIBI (Sistem Isyarat Bahasa Indonesia)

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Introduction

This project provides a set of utilities for preprocessing images and perform letter level SIBI realtime recogniton.
trained using [YOLO](https://github.com/ultralytics/ultralytics) V11, training type = Classsification

This project only cover 24 letter (A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y)
letter J and Z require motion detection cannot be implemeted in this project

## Usage

1. Install all requirements
2. If want train new model --> Run training.py
3. to start the program --> Run inference.py
4. OpenCV interface will automatically open
5. show sign language gesture to camera

## Requirements

- [Python 3.11](https://www.python.org/downloads/release/python-3119//)
- [Ultraliytics YoloV11](https://github.com/ultralytics/ultralytics)

## Installation

- create virtual environment

```shell
python -3.11 -m venv venv
```

- activate environment

```shell
venv/Scripts/activate
```

- Install all dependencies

```shell
pip install -r requirements.txt

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
