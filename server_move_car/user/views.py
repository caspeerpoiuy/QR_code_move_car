from django.http import HttpResponse,JsonResponse
from user.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    jsonloads = (json.loads(request.body.decode(encoding='utf-8')))
    username = jsonloads['username']
    password = jsonloads['password']
    confirm_password = jsonloads['confirm_password']
    if not all([username,password,confirm_password]):
        return JsonResponse({"code": 1, "msg": "数据不完整"})
    if password != confirm_password:
        return JsonResponse({"code":1,"msg":"密码两次输入不一致"})
    isexist = User.objects.check_username(username)
    if isexist:
        return  JsonResponse({"code":1,"msg":"用户名已存在"})
    try:
        User.objects.add_one_user(username,password)
    except Exception as e:
        print(e)
    return JsonResponse({"code":0,"data":"注册成功"})

@csrf_exempt
def login(request):
    jsonloads = (json.loads(request.body.decode(encoding='utf-8')))
    username = jsonloads['username']
    password = jsonloads['password']
    if not all([username,password]):
        return JsonResponse({"code": 1, "msg": "数据不完整"})
    isexist = User.objects.check_username(username)
    if not isexist:
        return JsonResponse({"code": 1, "msg": "用户名不存在"})
    user = User.objects.get_one_user(username,password)
    if not user:
        return JsonResponse({"code": 1, "msg": "密码错误"})
    return JsonResponse({"code": 0, "msg": "ok"})