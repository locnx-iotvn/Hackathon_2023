# CCBot - For Chinese Chess (XiangQi)

Building a robot that can play Chinese chess (XiangQi) with humans.

![CCBot](./docs/images/banner.png)

- Main Code: `chesssai`.
- Deep Learning / Data Preparation: `dnn_models/data_preparation`.
- Deep Learning / Training: `dnn_models/training`.

**Prototype 01**
![Prototype 01](./docs/images/prototype_01.jpg)

## 1. Project roadmap

- [x] Object detection model for chess pieces.
- [x] Board alignment and perspective crop.
- [x] Chinese chess board position detection.
- [x] Add chess engine ([./godogpaw](godogpaw)).
- [ ] Code for controlling the robot arm.
- [ ] Add 3D design.
- [ ] Add 3D printing files.
- [ ] Add documentation.
- [ ] Support for other chess variants.

## 2. Environment setup

- Clone this repository.

```bash
git clone https://github.com/vietanhdev/chessai --recursive
```

- Python >= 3.9.

```bash
pip install -r requirements.txt
```

Or using `Conda`:

```bash
conda create -n chessai python=3.9
conda activate chessai
pip install -r requirements.txt
```

## 3. Build chess engine

- This project uses [godogpaw](https://github.com/hmgle/godogpaw) as the chess engine.
- Install [Go](https://go.dev/doc/install).
- Build the engine.

```bash
cd godogpaw
go build
```

- Copy the executable file (`godogpaw*`) to the [./data/engines](./data/engines) folder.

## 4. Usage

```bash
ENGINE_PATH="data/engines/godogpaw-macos-arm" python main.py
```

Replace `ENGINE_PATH` with the path to the chess engine executable file.

- Press `ESC` to quit.
- Press `m` to get move from chess engine.

## 5. Data preparation & Training

This project uses computer vision and deep learning to detect chess pieces and chess board position.

**AI flow for chess detection**
![AI flow for chess detection](./docs/images/ai_flow.png)

- Go to [dnn_models](./dnn_models) folder and follow the instructions in the `README.md` file.

## 6. References

- This project was initially built for [Hackster's OpenCV AI Competition 2023](https://www.hackster.io/contests/opencv-ai-competition-2023). Hackster Project: [CCBot - Chinese Chess (XiangQi) robot with Vision](https://www.hackster.io/vietanhdev/ccbot-chinese-chess-xiangqi-robot-with-vision-4be768).
- Object detection model (for chess pieces) is based on [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX).
