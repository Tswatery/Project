from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import UserInfo


# Create your views here.

def index(request):
    return render(request, "index.html")


def user_list(request):
    # 去templates目录下找user_list.html(根据app的注册顺序 逐一寻找)
    return render(request, "user_list.html")


def news(request):
    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        "Referer": "https://www.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    response = requests.get("https://www.chinaunicom.cn/api/article/NewsByIndex/2/2023/09/news", headers=headers)

    print(response.json())
    return render(request, "news.html", {"info_list": response.json()})


def something(request):
    # request是一个对象 里面封装了所有请求相关数据
    # request.method
    # request.GET 获取url的后缀
    # request.POST 获取post的信息
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # POST
        print(request.POST)
        return HttpResponse("登录成功")


'''
展示所有的用户
'''


def info_list(request):
    # 1 获取数据库中所有的用户信息
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name=user, password=pwd, age=age)
    return redirect("http://127.0.0.1:8000/info_list")


def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/info_list")