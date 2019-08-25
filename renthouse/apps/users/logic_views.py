# file : logic_views.py
# author : ytouch
# date : 2019.08.25
# description: a basic logic views to console put/get/post/delete methods
# version: v1.0.0
# update info:

from django.shortcuts import render
from .models import UserModel
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .basic_tools import checkUserLoginInfo

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
        json_Result = checkUserLoginInfo(username_str,password_str)
        if (json_Result['OK'] == 0):
            return Response(json_Result['error'])
        userdata = UserModel.objects.all()
        serializer = UserSerializer(userdata,many=True)
        print(type(serializer.data))
        print(type(serializer))
        return Response(serializer.data)