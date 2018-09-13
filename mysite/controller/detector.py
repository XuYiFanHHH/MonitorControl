# coding=utf-8
from yolov3.yolo import YOLO


yolo = None
isBegin = True
isWarning = False
left = 0
top = 0
right = 0
bottom = 0

if yolo is None:
    yolo = YOLO()
