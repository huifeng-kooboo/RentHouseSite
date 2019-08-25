# file : logic_views.py
# author : ytouch
# date : 2019.08.25
# description: a basic logic views to console put/get/post/delete methods
# version: v1.0.0
# update info:

from django.shortcuts import render
from .models import UserModel
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .basic_tools import checkUserLoginInfo,generateSecurityPassword,checkSecurityPassword
import json

class LoginView(APIView):
    '''
    @description: a basic method to console login page
    @author: ytouch
    '''
    def post(self,request,*args,**kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return: json type :that whether login success
        '''
        # get fronted data
        username_str = request.data.get('username')
        password_str = request.data.get('password')
        is_admin_str = request.data.get('is_admin')
        json_Result = checkUserLoginInfo(username_str,password_str)
        '''用户名或密码不符合要求时'''
        if json.loads(json_Result)['OK'] == 0:
            return Response(json.loads(json_Result)['error'],status=status.HTTP_400_BAD_REQUEST) #错误请求
        userdata = UserModel.objects.all()
        '''检查数据库是否存在重复用户名'''
        '''生成加密密码'''
        password_sec = generateSecurityPassword(password_str) # generate security password
        '''save to database'''
        serializer = UserSerializer(userdata,many=True)
        return Response(serializer.data)