# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic serialize to jsontype
# version: v1.0.0
# update info:

from .models import UserModel,HouseInfoModel,AddPhotoModel
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @用户序列化，用于注册时候调用
    '''
    class Meta:
        model = UserModel
        fields = ('username','password','is_admin','phone_number','rent_address','idcard')

class HouseInfoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief: 暂时无用，日后处理
    '''
    class Meta:
        model = HouseInfoModel
        fields = ('house_images','house_title','basic_interviews','house_price',
                  'house_position','connect_phone','renter_name')

class BriefHouseInfoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief: 展示给大厅主页的房源信息内容，包括了房源图片和房源title两个内容。
    '''
    class Meta:
        model = HouseInfoModel
        fields = ('house_images','house_title')

class AddPhotoModelSerializer(serializers.ModelDurationField):
    '''
    @brief: 暂时无用，日后处理
    '''
    class Meta:
        model = AddPhotoModel
        fields = ('photos')