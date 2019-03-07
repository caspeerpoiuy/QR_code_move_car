from django.http import HttpResponse,JsonResponse
from user.models import User
from django.views.decorators.csrf import csrf_exempt


def register(request):
    print(request.POST)
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    confirm_password = request.POST.get('confirm_password')
    print(username,password,confirm_password)
    if not all([username,password,confirm_password]):
        return JsonResponse({"code": 1, "msg": "数据不完整"})
    if password != confirm_password:
        return JsonResponse({"code":1,"msg":"密码两次输入不一致"})
    isexist = User.object.check_username(username)
    if isexist:
        return  JsonResponse({"code":1,"msg":"用户名已存在"})

    User.object.add_one_user(username,password)
    return JsonResponse({"code":0,"msg":"注册成功"})
