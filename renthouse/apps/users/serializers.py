# file : models.py
# author : ytouch
# date : 2019.08.25
# description: a basic serialize to jsontype
# version: v1.0.0
# update info:

from .models import UserModel
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username','password','is_admin','phone_number','rent_address','idcard')

