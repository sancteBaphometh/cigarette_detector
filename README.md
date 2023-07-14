# cigarette_detector

Содержит два скрипта - image_detect.py и video_detect.py. Первый для предсказания и отрисовки bounding boxes на фото, второй - для видео.

Пример запуска скрипта через командную строку: **_python image_detect.py "in_image.jpg" "out_image.jpg"_**.

Отработав, скрипт создаёт медиафайл с отрисованными bounding boxes по пути "content/processed/".

---
# Результаты работы

Как видно на представленном ниже фото, обученная модель не блещет качеством. Возможно нужно собрать тренировочный датасет побольше, добавить аугментаций или поподбирать гиперпараметры.

![Иллюстрация 1](https://github.com/sancteBaphometh/cigarette_detector/blob/main/PR_curve.png)

Ниже представлен пример работы на одном из батчей фотографий, сверху размеченные мной,

![Иллюстрация 2](https://github.com/sancteBaphometh/cigarette_detector/blob/main/val_batch1_labels.jpg)

 снизу предсказанные моделью.

![Иллюстрация 3](https://github.com/sancteBaphometh/cigarette_detector/blob/main/val_batch1_pred.jpg)
