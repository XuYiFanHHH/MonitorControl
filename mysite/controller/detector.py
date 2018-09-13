# coding=utf-8
from yolov3.yolo import YOLO

known_face_encodings = None
known_face_names = None

yolo = None
isBegin = True

if yolo is None:
    yolo = YOLO()


