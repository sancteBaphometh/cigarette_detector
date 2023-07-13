from ultralytics import YOLO
from pathlib import Path
import cv2
import argparse

''' Создаём парсер для кастомных команд в CLI '''
parser = argparse.ArgumentParser(description="Type a source video name and a final video name (e.g. \"video.mp4\" \"processed_video.mp4\")")

# Название исходного видео
parser.add_argument(
    "vidname",
    type=str,
    help="Enter a sourse video name"
)

# Название выходного видео
parser.add_argument(
    "finvidname",
    type=str,
    help="Enter a final video name"
)

args = parser.parse_args()

# Подгружаем модель
model = YOLO("best.pt")

''' Задаём параметры видео для передачи в VideoWriter '''
SOURCE_VIDEO_PATH = Path("content", "raw", args.vidname)
PROCESSED_VIDEO_PATH = Path("content", "processed", args.finvidname)

video_in = cv2.VideoCapture(str(SOURCE_VIDEO_PATH))
fps = video_in.get(cv2.CAP_PROP_FPS)
width = int(video_in.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_in.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

''' Передаём параметры в VideoWriter '''
video_out = cv2.VideoWriter(str(PROCESSED_VIDEO_PATH), fourcc, fps, (width, height))

''' Покадрово обрабатываем видео '''
while video_in.isOpened():
    ret, frame = video_in.read()
    if ret:
        frame = model(frame)
        frame = frame[0].plot()
        video_out.write(frame)
    else:
        break
video_in.release()
video_out.release()