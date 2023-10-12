## templates模版

其实就是html文件，也就是转发到对应路由后服务情返回的html文件。

## 静态文件

### 如何在模版中引用？





## 文件结构

```
.
└── DjangoBili
    ├── DjangoBili
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-311.pyc
    │   │   └── settings.cpython-311.pyc
    │   ├── asgi.py											【网络异步相应 基本不用管】
    │   ├── settings.py									【Django的配置项，有些app的注册要在这列写】
    │   ├── urls.py											【路由转发里面写了'/index'，当访问www.xxx.com/index就返回对应的视图函数】
    │   └── wsgi.py											【同步响应】
    ├── app01
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py										【模版】
    │   ├── tests.py
    │   └── views.py										【视图函数 对应urls.py中的视图函数】
    └── manage.py												【Django的启动文件】
```



## 请求和响应

### 重定向

比如：

```python
def Redirect(request):
  return redirect("https://www.baidu.com")
```

提供两种选择：

1. 浏览器向服务器发起对应请求，然后服务器再去获取百度页面返回给浏览器；
2. 浏览器向服务器发起对应请求，服务器返回重定向地址，浏览器自行去访问百度页面。 ✅

## 数据库操作

Django内部有自己的数据库对象，称为orm。orm其实是代码和数据库中间的一个组件，能够翻译代码，让代码更加简洁。

### 案例 用户管理

1. 展示用户列表
2. 添加用户
   1. GET请求，看到页面；
   2. POST请求，提交-》写入数据库。