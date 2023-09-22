# ChessAI Training

```shell
conda create -n chessai python=3.9 -y
```

```shell
conda activate chessai-training
```

```shell
cd dnn_models/training
conda activate chessai-training
pip install torch==2.0.1
pip install -e .
```

```text
+ datasets
    + chessai
        + COCO
            + annotations
                - train.json
                - val.json
            + images
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

```shell
python tools/train.py 
```
