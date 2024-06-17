# Realtime Sign Language Recignition for SIBI (Sistem Isyarat Bahasa Indonesia)

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Introduction

This project provides a set of utilities for preprocessing images and perform letter level SIBI realtime recogniton.
trained using [YOLO](https://github.com/ultralytics/ultralytics) V8, training type = Classsificartion

## Usage

1. Install all requirements
2. If you have basic Requirement --> Run yoloGradio.py
3. If you have Advanced Requirement --> Run yoloOnnx.py
4. Open local URL: http://127.0.0.1:7860 and ensure you have webcam on your device

## Requirements

- [Python 3.x](https://www.python.org/)
- gradio
  ```cli
  pip install gradio
  ```
- ultralytics
  ```cli
  pip install ultralytics
  ```
- Pytorch
  ```cli
  pip install torch
  ```

### Advanced Requirements

- opencv-python
  ```cli
  pip install opencv-python
  ```
- onnx
  ```cli
  pip install onnx
  ```
- onnxruntime
  ```cli
  pip install onnxruntime
  ```
- numpy
  ```cli
  pip install numpy
  ```

## Installation

this prgoram is ready to go, just make sure you have all requirements fulfilled.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
