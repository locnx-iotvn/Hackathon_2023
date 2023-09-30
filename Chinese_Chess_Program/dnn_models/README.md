# Training for DNN models

## 1. Data preparation

- Go to `data_preparation` folder and follow the instructions in the README.md file.
- Copy the generated data to `training/datasets/chessai` folder.

```
dnn_models/data_preparation/data/train.json >> dnn_models/training/datasets/chessai/COCO/annotations/train.json
dnn_models/data_preparation/data/val.json >> dnn_models/training/datasets/chessai/COCO/annotations/val.json
dnn_models/data_preparation/data/combined_data >> dnn_models/training/datasets/chessai/COCO/train
dnn_models/data_preparation/data/combined_data >> dnn_models/training/datasets/chessai/COCO/val
```

## 2. Training

- Follow the instructions in the README.md file in `training` folder.
