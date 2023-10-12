from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

'''
一读到这个类，底层orm就会帮我们创建一张表
create table app01_userinfo(
    id bigint auto_increment primary key, (django 自动生成的)
    name varchar(32),
    password varchar(64),
    age int
)
'''
