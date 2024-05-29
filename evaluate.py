# Load YOLOv8n

import torch

from multiprocessing import freeze_support

from ultralytics import YOLO

model = YOLO('model_A.pt')  


def run():
    metrics = model.val()
    

if __name__ == '__main__':
    run()
