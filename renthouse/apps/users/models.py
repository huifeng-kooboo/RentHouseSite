# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic models
# version: v1.0.0
# update info:

from django.db import models

# Create your models here.
class UserModel(models.Model):
    '''
    @description: login table for users
    @author:ytouch
    @email:gisdoing@gmail.com
    '''
    username = models.CharField(default='',unique=True,verbose_name='用户名',max_length=20,primary_key=True) # username: primary_key
    password = models.CharField(default='', verbose_name='密码', max_length=100) # password: member
    is_admin = models.BooleanField(default=False,verbose_name="是否为管理员") # is_admin: member
    class Meta:
        db_table = 'user_table'  #@comment : db_table means create a table_name 'user_table'
        verbose_name = '用户信息表'