from django.http import JsonResponse, StreamingHttpResponse,HttpResponse
from django.views.decorators.http import require_http_methods
import math
import time
import  numpy as np
import  cv2 as cv
from .opencv_utils import capture_pic, VideoCamera
from PIL import Image
from .models import UserInfo, WarningHistory
from .detector import yolo, isBegin, known_face_encodings, known_face_names, terroristWarning, forbiddenAreaWarning, left, top ,right, bottom, terroristName, last_facerec_time
import face_recognition
import os
from timeit import default_timer as timer
import pickle
import threading

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


def state_gen():
    while True:
        data = {"name": "Lee"}
        yield data


def long_polling(request):
    global forbiddenAreaWarning, data, terroristWarning, terroristName
    forbiddenAreaWarning = False
    terroristWarning = False
    terroristName = []
    while True:
        if terroristWarning == True and forbiddenAreaWarning == False:
            terroristWarning = False
            nameList = ''
            for name in terroristName:
                nameList = nameList + ' ' + name
            temp = []
            temp.append(nameList + ' appeared')
            return JsonResponse({'Type': temp})
        elif terroristWarning == False and forbiddenAreaWarning == True:
            forbiddenAreaWarning = False
            temp = ['person appeared in forbidden area']
            return JsonResponse({'Type': temp})
        elif terroristWarning == True and forbiddenAreaWarning == True:
            terroristWarning = False
            forbiddenAreaWarning = False
            terroristWarning = False
            nameList = ''
            for name in terroristName:
                nameList = nameList + ' ' + name
            temp=[]
            temp.append(nameList+' appeared')
            temp.append('persion appeared in forbidden area')
            return JsonResponse({"Type":temp})
        else:
            time.sleep(1)


@require_http_methods(["POST"])
def setRect(request):
    global left, top, right, bottom
    left = request.POST['bPoint0']
    top = request.POST['bPoint1']
    right = request.POST['ePoint0']
    bottom = request.POST['ePoint1']
    print("(%s,%s)(%s,%s)"%(left,top,right,bottom))

    return JsonResponse({"data":"success"})

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
    global known_face_encodings, terroristWarning, terroristName
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
    print('person match', terroristName)
    #检测结果中有已知的人
    if name != 'Unknown':
        warningtype = 'found person of warning list'
        warningcontent = name + " appeared"
        if name not in terroristName:
            terroristName.append(name)
        terroristWarning = True
        warning = WarningHistory(warningtype = warningtype, warningcontent = warningcontent)
        warning.save()

def isIntersect(x01, x02, y01, y02, x11, x12, y11, y12):
    zx = abs(x01 + x02 - x11 - x12);
    x = abs(x01 - x02) + abs(x11 - x12);
    zy = abs(y01 + y02 - y11 - y12);
    y = abs(y01 - y02) + abs(y11 - y12);
    if zx <= x and zy <= y:
        return True
    else:
        return False


def gen(camera):
    global isBegin, left, top, right, bottom, forbiddenAreaWarning, last_facerec_time
    while True:
        start = timer()
        global isBegin, data
        if not isBegin:
            break
        image = camera.get_array_frame()
        image = Image.fromarray(image)
        # 物体检测
        im, labels, locations = yolo.detect_image(image)
        # 若有人脸，截取出来进行检测
        if len(locations) > 0:
            for location in locations:
                forbiddenAreaWarning = isIntersect(int(left), int(right), int(top), int(bottom), location[0], location[2],
                                        location[1], location[3])
                if forbiddenAreaWarning == True:
                    warningtype = 'person in forbidden area'
                    warningcontent = 'person appeared in forbidden area'
                    warning = WarningHistory(warningtype=warningtype, warningcontent=warningcontent)
                    warning.save()
                    data = 'person appeared in forbidden area'
                print(labels)
                print(locations)
                # recognizeFace(image.crop(location))
                thisTime = timer()
                if (thisTime - last_facerec_time) >= 2:
                    t =threading.Thread(target=recognizeFace,args=(image.crop(location),))
                    t.start()
                    last_facerec_time = thisTime
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
    global isBegin, last_facerec_time
    isBegin = True
    last_facerec_time = timer()
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

@require_http_methods(["POST"])
def add_warning(request):
    response = {}    
    try:        
        warningtype = 'found person of warning list'
        warningcontent = "appeared"
        warning = WarningHistory(warningtype = warningtype, warningcontent = warningcontent)
        warning.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    print(response)
    return JsonResponse(response)

@require_http_methods(["POST"])
def delete_warning(request):
    response = {}    
    try:        
        warningId = int(request.POST["id"])
        warning = WarningHistory.objects.filter(id = warningId)
        warning.delete()   
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    print(response)
    return JsonResponse(response)

@require_http_methods(["POST"])
def get_onepage_warnings(request):
    response = {}    
    global isBegin
    isBegin = False
    try:
        pageId = int(request.POST["page"])
        
        total_news_num = WarningHistory.objects.all().count()
        # 一页显示二十条
        pages = math.ceil(total_news_num / 20)
        response['pages'] = pages

        start_num = (pageId - 1) * 20
        end_num = start_num + 20
        if end_num > total_news_num:
            end_num = total_news_num
        List = list(WarningHistory.objects.all().values()[start_num:end_num])
        resultList = []
        for item in List:
            resullItem = {  'id': item['id'], 
                            'warningtype': item['warningtype'],
                            'warningcontent': item['warningcontent'],
                            'warningtime': item['addtime']}
            resultList.append(resullItem)
        response['list'] = resultList
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)