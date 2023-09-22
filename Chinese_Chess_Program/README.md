# ChessAI

AI for chess robot, starting with XiangQi (Chinese chess).

- Main Code: `chesssai`.
- Deep Learning / Data Preparation: `dnn_models/data_preparation`.
- Deep Learning / Training: `dnn_models/training`.

## TODO

- [x] Object detection model for chess pieces.
- [x] Board alignment and perspective crop.
- [x] Chinese chess board position detection.
- [ ] Add chess engine.
- [ ] Code for controlling the robot arm.
- [ ] Add 3D design.
- [ ] Add 3D printing files.
- [ ] Add documentation.
- [ ] Support for other chess variants.

## Environment Setup

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

## Build chess engine

- This project uses [godogpaw](https://github.com/hmgle/godogpaw) as the chess engine.
- Install [Go](https://go.dev/doc/install).
- Build the engine.

```bash
cd godogpaw
go build
```

- Copy the executable file (`godogpaw*`) to the [./data/engines](./data/engines) folder.

## Usage

```bash
ENGINE_PATH="data/engines/godogpaw-macos-arm" python main.py
```

Replace `ENGINE_PATH` with the path to the chess engine executable file.

- Press `ESC` to quit.
- Press `m` to get move from chess engine.

## References

- This project was initially built for [Hackster's OpenCV AI Competition 2023](https://www.hackster.io/contests/opencv-ai-competition-2023). Hackster Project: [CCBot - Chinese Chess (XiangQi) robot with Vision](https://www.hackster.io/vietanhdev/ccbot-chinese-chess-xiangqi-robot-with-vision-4be768).
- Object detection model was trained using [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX).
