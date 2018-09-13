from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
import math
import time
import  numpy as np
import  cv2 as cv
from .opencv_utils import capture_pic, VideoCamera
from PIL import Image
from .models import UserInfo
from .detector import yolo, isBegin, known_face_encodings, known_face_names
import face_recognition
import os
from timeit import default_timer as timer
import pickle

# Create your views here.

@require_http_methods(["POST"])
def login(request):
    response = {}    
    # 已经登录
    if 'username' in request.COOKIES.keys():
        print("already login")
        response['msg'] = "already login"
        response['error_num'] = 1
        response = JsonResponse(response)
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            objectList = list(UserInfo.objects.filter(username = username).values())
            if len(objectList) > 0 and objectList[0]['password'] == password:
                global isBegin
                isBegin = True
                response['msg'] = "success"
                response['error_num'] = 0
                response = JsonResponse(response)
                response.set_cookie(key= 'username', value= username, max_age=3600)
            else:
                response['msg'] = "username or password error"
                response['error_num'] = 1
                response = JsonResponse(response)
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
            response = JsonResponse(response)
    return response

@require_http_methods(["POST"])
def register(request):
    response = {}    
    try:
        username = request.POST['username']
        password = request.POST['password']
        objectList = list(UserInfo.objects.filter(username = username).values())
        if len(objectList) > 0:
            print("该用户已存在")
            obj = UserInfo.objects.get(username='username')
            obj.password = password
            obj.save()
            response['msg'] = "success"
            response['error_num'] = 0
            response = JsonResponse(response)
        else:
            print("该用户未存在")
            obj = UserInfo(username = username, password = password)
            obj.save()
            response['msg'] = "success"
            response['error_num'] = 0
            response = JsonResponse(response)
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        response = JsonResponse(response)
    return response

@require_http_methods(["POST"])
def logout(request):    
    response = {}    
    # 已经登录
    if 'username' in request.COOKIES.keys():
        global isBegin
        isBegin = False
        response['msg'] = "success"
        response['error_num'] = 0
        response = JsonResponse(response)
        response.delete_cookie('username')
    else:
        response['msg'] = "have not login"
        response['error_num'] = 1
        response = JsonResponse(response)
    return response

@require_http_methods(["POST"])
def changePwd(request):
    response = {}    
    if 'username' in request.COOKIES.keys():
        try:
            username = request.POST['username']
            password = request.POST['password']
            newPassWord = request.POST['newPassWord']
            objectList = list(UserInfo.objects.filter(username = username).values())
            if request.COOKIES['username'] == username and len(objectList) > 0 and objectList[0]['password'] == password:
                print("该用户已存在")
                obj = UserInfo.objects.get(username= username)
                obj.password = newPassWord
                obj.save()
                response['msg'] = "success"
                response['error_num'] = 0
                response = JsonResponse(response)
            else:
                print("该用户未存在")
                response['msg'] = "username or password error or this user doesn't exist"
                response['error_num'] = 1
                response = JsonResponse(response)
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
            response = JsonResponse(response)
    else:
        response['msg'] = 'you have not login'
        response['error_num'] = 100
        response = JsonResponse(response)
    return response
# 识别人脸
def recognizeFace(targetImg):
    global known_face_names
    global known_face_encodings
    # 初始化已知人脸
    if known_face_names is None:       
        with open("face_encodings.pickle","rb") as f:
            data = pickle.load(f)
            known_face_names = data["known_face_names"]
            known_face_encodings = data["known_face_encodings"]
    start = timer()
    targetImg = targetImg.resize((250,250))
    targetImg = targetImg.convert(mode = 'RGB')         
    targetImgArray = np.array(targetImg)
    face_encoding_list = face_recognition.face_encodings(targetImgArray)
    name = "Unknown"
    # 有可能dlib在该图片中找不到人脸
    if len(face_encoding_list) > 0:
        face_encoding = face_encoding_list[0]
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]  
    end = timer()
    print("facerec time:", end - start)             
    print('person match', name)

def gen(camera):
    global isBegin
    while True:
        # print(isBegin)
        start = timer()
        if not isBegin:
            break
        image = camera.get_array_frame()
        image = Image.fromarray(image)
        # 物体检测
        im, labels, locations = yolo.detect_image(image)
        # 若有人脸，截取出来进行检测
        if len(locations) > 0:
            for location in locations:
                recognizeFace(image.crop(location))
        # 生成器产生带框图片返回给前端
        im = im.resize((640,480))
        im = np.array(im)
        ret, jpeg = cv.imencode('.jpg', im)
        frame = jpeg.tobytes()
        end = timer()
        print("total time:", end - start)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def send_image(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')