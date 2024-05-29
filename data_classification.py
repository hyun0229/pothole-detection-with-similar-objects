import json
import os
from pathlib import Path
import shutil
from PIL import Image

#AIhub의 데이터를 분류하고 Yolov8의 format으로 변경하여 저장함

def xywh2yolo(bbox, img_width, img_height):
    cx, cy, w, h = bbox
    x_center = (cx+w/2) / img_width
    y_center = (cy+h/2) / img_height
    width = w / img_width
    height = h / img_height
    return [x_center, y_center, width, height]

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height
    
def check_category_combinations(annotations, combinations):
    categories_in_file = {anno['category_id'] for anno in annotations}
    for combination in combinations:
        if combination.issubset(categories_in_file):
            return True
    return False

def check_category_combinations(annotations, combinations):
    categories_in_file = {anno['category_id'] for anno in annotations}
    for combination in combinations:
        if combination.issubset(categories_in_file):
            return True
    return False

def convert_to_yolo_format(src_json_dir, src_img_dir, dest_dir, combinations):
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    json_files = [file for file in os.listdir(src_json_dir) if file.endswith('.json')]
    
    for json_file in json_files:
        with open(os.path.join(src_json_dir, json_file), 'r') as file:
            data = json.load(file)

        if check_category_combinations(data['annotations'], combinations):
            img_file_name = data['images']['file_name']
            img_path = os.path.join(src_img_dir, img_file_name)
            img_width, img_height = get_image_dimensions(img_path)

            yolo_data = []
            for anno in data['annotations']:
                if anno['category_id'] in {8, 9, 10}: 
                    bbox = xywh2yolo(anno['bbox'], img_width, img_height)
                    yolo_line = f"{anno['category_id'] - 8} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}"
                    yolo_data.append(yolo_line)

            if yolo_data:
                yolo_file_path = os.path.join(dest_dir, img_file_name.split('.')[0] + '.txt')
                with open(yolo_file_path, 'w') as f:
                    f.write('\n'.join(yolo_data))


                dest_image_path = os.path.join(dest_dir, img_file_name)
                shutil.copy2(img_path, dest_image_path)

# Paths
src_img_dir = '5.Mainroad_A01_img' 
src_json_dir = '5.Mainroad_A01_json'
dest_dir = 'classified_data'
combinations = [{8,9},{8,9,10},{8,10}]

convert_to_yolo_format(src_json_dir, src_img_dir, dest_dir, combinations)
