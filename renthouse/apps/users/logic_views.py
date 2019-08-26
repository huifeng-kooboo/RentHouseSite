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
        '''Error Type Password Or UserName'''
        if json.loads(json_Result)['OK'] == 0:
            return Response(json.loads(json_Result)['error'],status=status.HTTP_400_BAD_REQUEST) #错误请求
        userdata = UserModel.objects.filter(username=username_str)
        if len(userdata) < 1:
            return Response('当前用户名不存在,请重新输入',status=status.HTTP_400_BAD_REQUEST)
        cur_password_str = userdata[0].password
        b_password =checkSecurityPassword(password_str,cur_password_str) # compare the password
        if b_password == False:
            return Response('密码错误,请重新输入',status=status.HTTP_400_BAD_REQUEST)
        return Response('登录成功',status=status.HTTP_200_OK)

class RegisterView(APIView):
    '''
    @description: a basic method to console register page
    @author: ytouch
    '''
    def post(self,request,*args,**kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # get fronted data
        username_str = request.data.get('username')
        password_str = request.data.get('password')
        phone_number_str = request.data.get('phone_number')
        rent_address_str = request.data.get('rent_address')
        idcard_str = request.data.get('idcard')
        # check whether true
        json_Result = checkUserLoginInfo(username_str,password_str)
        '''Error Type Password Or UserName'''
        if json.loads(json_Result)['OK'] == 0:
            return Response(json.loads(json_Result)['error'],status=status.HTTP_400_BAD_REQUEST) #错误请求
        cur_password = generateSecurityPassword(password_str) #密码加密
        userdata_count = UserModel.objects.filter(username=username_str)
        if len(userdata_count) > 0:
            return Response('当前用户已注册，请返回登录！',status=status.HTTP_400_BAD_REQUEST)
        userdata = UserModel.objects.create(username=username_str,password=cur_password,is_admin=False,idcard=idcard_str,rent_address=rent_address_str,phone_number=phone_number_str)
        return Response('注册成功',status=status.HTTP_200_OK)