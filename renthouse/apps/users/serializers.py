# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic serialize to jsontype
# version: v1.0.0
# update info:

from .models import UserModel,HouseInfoModel
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username','password','is_admin','phone_number','rent_address','idcard')

class HouseInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HouseInfoModel
        fields = ('house_images','basic_interviews','house_price',
                  'house_position','connect_phone','renter_name')
