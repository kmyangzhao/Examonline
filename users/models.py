# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


#继承AbstractBaseUser扩展用户信息表
class UserProfile(AbstractUser):
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="female")
    mobile = models.CharField(max_length=11,null= True,blank=True)


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self): #python2 __unicode__
        return self.username


#邮箱验证
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

#首页轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#部门信息
class DeptProfile(models.Model):
    deptname = models.CharField(max_length=50, verbose_name=u"部门名称")
    deptlevel = models.SmallIntegerField(verbose_name=u"部门层级")
    parentid = models.CharField(max_length=32, verbose_name=u"父节点ID")
    is_active = models.BooleanField(default=True,verbose_name=u"是否激活")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        verbose_name = u"部门信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.deptname




