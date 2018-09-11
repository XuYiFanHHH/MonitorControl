from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
import math

from .models import UserInfo
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
        response['msg'] = "success"
        response['error_num'] = 0
        response = JsonResponse(response)
        response.delete_cookie('username')
    else:
        response['msg'] = "have not login"
        response['error_num'] = 1
        response = JsonResponse(response)
    return response