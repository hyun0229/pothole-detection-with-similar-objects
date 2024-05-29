# Load YOLOv8n

import torch

from multiprocessing import freeze_support

from ultralytics import YOLO

model = YOLO('yolov8m.pt')  

def run():
    
    torch.multiprocessing.freeze_support()
      # 모델 훈련
    model.train(data='data.yaml', epochs=100, patience=30, batch=16, imgsz=640)


if __name__ == '__main__':
    run()
