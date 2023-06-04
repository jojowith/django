# -*-coding:utf-8-*-
from django.db import models
# Create your models here.
class Department(models.Model):
    """部焚表"""
    title= models.CharField(verbose_name='部門',max_length=32)

class UserInfo(models.Model):
    """用戶表"""
    name= models.CharField(verbose_name="姓名", max_length=16)
    password= models.CharField(verbose_name='密碼',max_length=64)
    age=models.IntegerField(verbose_name='年寧')
    account= models.DecimalField(verbose_name='帳戶餘額',max_digits=10, decimal_places=2, default=0)
    create_time= models.DateTimeField(verbose_name='入職時間')

    depart= models.ForeignKey(to=Department,to_field='id', on_delete=models.CASCADE)

    gender_choices=(
        (1,'男'),
        (2,'女'),
    )
    gender= models.SmallIntegerField(verbose_name='性別', choices=gender_choices)
