"""
URL configuration for DjangoBili project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

# url和python函数的对应关系

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('index/', views.index),  # 表示用户访问www.xxx.com/index就会执行后面的函数(一般在views中)
    path('user_list/', views.user_list),
    path('news/', views.news),
    path('something', views.something),
    path('login/', views.login),

    # 用户管理
    path('info_list/', views.info_list),
    path('add_user/', views.info_add),
    path('delete_user/', views.info_delete)
]
