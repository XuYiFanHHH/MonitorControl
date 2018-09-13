import cv2 as cv

url = "rtsp://admin:admin@59.66.68.38:554/cam/realmonitor?channel=1&subtype=0"
cap = cv.VideoCapture(0)

def  get_array_frame():
    _, image = cap.read()
    return image   