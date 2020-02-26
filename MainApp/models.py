from datetime import datetime
from django.db import  models

# Create your models here.


class Datas(models.Model):
    zhujue = models.CharField(max_length=64, verbose_name="主角", default="美女")
    poster = models.CharField(max_length=256,verbose_name="海报img")
    url = models.CharField(max_length=512, verbose_name="目标链接")
    tags = models.CharField(max_length=32,verbose_name="标签分类")
    addtime = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")
    fromuser = models.CharField(max_length=64, verbose_name="上传者",default="Manager")
    title = models.CharField(max_length=64,verbose_name="标题",default="美女")
    jieshao = models.CharField(max_length=512,verbose_name="详情介绍")
    class Meta:
        verbose_name = "资源数据中心"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "fuck you!"


class Usesr(models.Model):
    name = models.CharField(max_length=32, verbose_name="昵称",)
    userfeature = models.CharField(max_length=64,verbose_name="session特征")
    phone = models.CharField(max_length=16,verbose_name="手机号")
    mail = models.CharField(max_length=64,verbose_name="邮箱")
    isVIP = models.BooleanField(default=False,verbose_name="是否会员")
    VIPactiveTime = models.DateTimeField(verbose_name="会员激活时间")
    VIPtimeout = models.DateTimeField(verbose_name="会员失效时间")
    isban = models.BooleanField(default=False,verbose_name="状态封禁状态")
    class Meta:
        verbose_name = "用户中心"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "you are bullshit"


