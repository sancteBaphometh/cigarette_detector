from ultralytics import YOLO
from pathlib import Path
import argparse
from matplotlib import pyplot as plt
import cv2
from PIL import Image

''' Создаём парсер для кастомных команд в CLI '''
parser = argparse.ArgumentParser(description="Type a source image name and a final image name (e.g. \"image.jpg\" \"processed_image.jpg\")")

# Название исходного изображения
parser.add_argument(
    "imname",
    type=str,
    help="Enter a sourse image name"
)

# Название выходного изображения
parser.add_argument(
    "finimname",
    type=str,
    help="Enter a final image name"
)

args = parser.parse_args()

# Подгружаем модель
model = YOLO("best.pt")

''' Задаём параметры видео для передачи в VideoWriter '''
SOURCE_IMAGE_PATH = Path("content", "raw", args.imname)
PROCESSED_IMAGE_PATH = Path("content", "processed", args.finimname)

res = model(SOURCE_IMAGE_PATH)
res_plotted = res[0].plot()

imageRGB = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
img = Image.fromarray(imageRGB)
img.save(str(PROCESSED_IMAGE_PATH))