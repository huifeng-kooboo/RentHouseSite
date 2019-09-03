from rest_framework import viewsets,mixins
from .models import UserModel,HouseInfoModel
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,HouseInfoSerializer
from .basic_tools import checkUserLoginInfo,checkSecurityPassword
from .signals import user_save
import json


class UserRegisterViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    @description:用户注册功能
    '''
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class AddHouseInfoViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):
    '''
    @brief :添加房源信息
    @remark:其中ListModelMixin：可以实现get请求，返回所有数据，前端进行处理展示给用户
    CreateModelMixin:负责post请求，创建新对象
    '''
    queryset = HouseInfoModel.objects.all()
    serializer_class = HouseInfoSerializer

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
            return Response(json.loads(json_Result)['error'],status=status.HTTP_400_BAD_REQUEST) #由前端做数据处理
        userdata = UserModel.objects.filter(username=username_str)
        print(type(userdata))
        if len(userdata) < 1:
            return Response('当前用户名不存在,请重新输入',status=status.HTTP_400_BAD_REQUEST) #由前端做数据处理
        cur_password_str = userdata[0].password
        b_password =checkSecurityPassword(password_str,cur_password_str) # compare the password
        '''b_password :True:密码正确，False:密码错误'''
        if b_password == False:
            return Response('密码错误,请重新输入',status=status.HTTP_400_BAD_REQUEST)
        request.session['login_name'] = username_str #设置登录session
        print(userdata.values())
        return Response(userdata.values()[0],status=status.HTTP_200_OK) #由前端做数据处理 userdata.values会直接转成json格式

