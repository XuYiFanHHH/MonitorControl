# coding=utf-8
from yolov3.yolo import YOLO

known_face_encodings = None
known_face_names = None

yolo = None
isBegin = True
isWarning = False
left = 0
top = 0
right = 0
bottom = 0

if yolo is None:
    yolo = YOLO()


