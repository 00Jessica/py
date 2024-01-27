from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Department
import json


def list_users(request):
    users = User.objects.all()  # 查询所有用户
    user_info = "<br>".join([f"姓名：{user.name}, 邮箱：{user.email}" for user in users])
    return HttpResponse(user_info)


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User(
            name=data["name"],
            gender=data["gender"],
            phone=data["phone"],
            email=data["email"],
            department=Department.objects.get(id=data["department"]),
            password=data["password"],
            is_admin="N",  # 默认设置为非管理员
        )
        user.save()
        return JsonResponse({"message": "用户注册成功"})
    return JsonResponse({"error": "请求方法不正确"}, status=400)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            user = User.objects.get(name=data["name"])
            if user.password == data["password"]:
                return JsonResponse({"message": "登录成功"})
            else:
                return JsonResponse({"error": "密码错误"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "用户不存在"}, status=404)
    return JsonResponse({"error": "请求方法不正确"}, status=400)


def login_view(request):
    return render(request, "filemanager/login.html")
