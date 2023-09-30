# ChessAI Training

## 1. Create conda environment

```shell
conda create -n chessai-training python=3.9 -y
```

```shell
conda activate chessai-training
```

```shell
cd dnn_models/training
pip install torch==2.0.1
pip install -e .
pip install tensorboard==2.12.0
```

## 2. Data preparation

```text
+ datasets
    + chessai
        + COCO
            + annotations
                - train.json
                - val.json
            - train
                - 000001.jpg
                - ...
            - val
                - 000001.jpg
                - ...
+ docs
+ exps
...
```

## 3. Training

```shell
export YOLOX_DATADIR=datasets/chessai
python tools/train.py 
```

Use `tmux` to run the training in the background.

## 4. Model export (to ONNX)

```shell
python tools/export_onnx.py -f exps/tfs_nano.py -c YOLOX_outputs/tfs_nano/best_ckpt.pth --output-name chessai-det.onnx
```

Copy `chessai-det.onnx` to `dnn_models/deployment/models`.
