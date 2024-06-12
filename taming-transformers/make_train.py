import os
import random

from pathlib import Path

random.seed(42)

image_cropped_path = "/opt/ml/DALLE-Couture/data/cropped_train_img"
image_path = Path(image_cropped_path)

image_files = [
    *image_path.glob("**/*.png"),
    *image_path.glob("**/*.jpg"),
    *image_path.glob("**/*.jpeg"),
]


random.shuffle(image_files)

train_image_files = image_files[:-10000]
with open("/opt/ml/taming-transformers/data/train_500k.txt", "w", encoding="utf-8") as f:
    for train_image_file in train_image_files:
        train_image_file = str(train_image_file) + "\n"
        f.write(train_image_file)

test_image_files = image_files[-10000:]
with open("/opt/ml/taming-transformers/data/test_500k.txt", "w", encoding="utf-8") as f:
    for test_image_file in test_image_files:
        test_image_file = str(test_image_file) + "\n"
        f.write(test_image_file)
