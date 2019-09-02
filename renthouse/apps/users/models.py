# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic models
# version: v1.0.0
# update info:

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    '''
    @description: login table for users
    @author:ytouch
    @email:gisdoing@gmail.com
    '''
    username = models.CharField(default='',unique=True,verbose_name='用户名',max_length=20,primary_key=True) # username: primary_key
    password = models.CharField(default='', verbose_name='密码', max_length=100) # password: member
    is_admin = models.BooleanField(default=False, verbose_name="是否为管理员")  # is_admin: member
    phone_number = models.CharField(default='',unique=True,verbose_name='手机号',max_length=11) # phonenumber
    rent_address = models.CharField(default='',verbose_name='住址',max_length=30) # 住址
    idcard = models.CharField(default='',unique=True,verbose_name='身份证',max_length=20) #身份证
    class Meta:
        db_table = 'user_table'  #@comment : db_table means create a table_name 'user_table'
        verbose_name = '用户信息表'
        ordering = ['-username']  #内部数据排序方式 根据username

class HouseInfoModel(models.Model):
    '''
    @brief ：添加房源信息model
    '''
    house_images = models.ImageField(verbose_name='房屋图片',upload_to='house/',blank=False,default='') #bug 上传多图片房屋图片
    basic_interviews = models.TextField(verbose_name='文字介绍',default='',blank=False)
    house_price = models.IntegerField(default=0,verbose_name='房屋价格',blank=False) # blank = False 表示字段不为空
    house_position = models.TextField(verbose_name='房屋地址',default='',blank=False)
    connect_phone = models.CharField(verbose_name='联系手机号',default='',max_length=20,blank=False) #联系手机号
    renter_name = models.TextField(verbose_name='业主姓名',default='',blank=False)
    class Meta:
        db_table = 'houseinfo_table' # 房屋信息表
        verbose_name = '房屋信息表'

class LandlordSetting(models.Model):
    '''
    @brief: 房东设置Model
    '''
    renter_name = models.TextField(verbose_name='房东姓名', default='', blank=False) # 默认添加为当前用户 不可修改
    rental_name = models.TextField(verbose_name='租客',max_length=222) # 租户不一样
    move_date = models.DateTimeField(verbose_name='入住时间')#设置入住时间
    is_net = models.BooleanField(verbose_name='是否有网费',default=True)
    net_fees = models.IntegerField(verbose_name='网费',default=30) #默认30
    ele_fees = models.IntegerField(verbose_name='电费') #电费
    water_fees = models.IntegerField(verbose_name='水费') #水费
    key_nums = models.IntegerField(verbose_name='钥匙数量') #钥匙数量
    is_condition = models.BooleanField(verbose_name='是否有空调')
    is_wash = models.BooleanField(verbose_name='是否有洗衣机') #洗衣机
    class Meta:
        verbose_name='房东设置表'
        db_table = 'landlord_table'
        # 租户信息自动每个月提醒，根据move_date :省了再建一个表，机智