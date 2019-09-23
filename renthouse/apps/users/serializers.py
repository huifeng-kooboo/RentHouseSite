# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic serialize to jsontype
# version: v1.0.0
# update info:

from .models import UserModel,HouseInfoModel,AddPhotoModel,LandlordManage,AdInfoModel
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
    @brief: 用于获取房源管理信息方便
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

class RenterBriefInfoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief:租户管理中显示租户姓名使用
    '''
    class Meta:
        model = UserModel
        fields = ('username','is_admin')

class LandloadManageSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief:房东设置的租户信息保存序列化
    '''
    class Meta:
        model = LandlordManage
        fields = ('tenant','rental_time','rental_address','rent_fee',
                  'water_fee','electric_fee','is_net','net_fee','key_num',
                  'is_air','is_washer') #设置需要保存的字段

class FeeListSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief:租户需要缴费的费用清单
    '''
    class Meta:
        model = LandlordManage
        fields = ('rent_fee','water_fee','electric_fee','net_fee')

class MyInfoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief:个人信息设置，包含需要展示给前端的东西,个人头像等后期再添加，也很简单
    '''
    class Meta:
        model = UserModel
        fields = ('username','phone_number','rent_address','idcard')

class AdPhotoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    @brief:广告数据库序列化字段
    '''
    class Meta:
        model = AdInfoModel
        fields = ('adphoto','id')
