from rest_framework import viewsets,mixins
from .models import UserModel,HouseInfoModel,AddPhotoModel
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,HouseInfoSerializer
from .basic_tools import checkUserLoginInfo,checkSecurityPassword
from .signals import user_save
import json
from django.core.cache import cache
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserRegisterViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    @description:用户注册功能
    '''
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

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
        return Response(userdata.values()[0],status=status.HTTP_200_OK) #由前端做数据处理 userdata.values[0]会直接转成json格式

class AddPhotoView(APIView):
    '''
    @description: save photo :只接受post请求
    @brief: 上传多张张图片功能
    @author: ytouch
    '''
    def post(self,request,*args,**kwargs):
        image = request.data['file']
        image_data = [image.file, image.field_name, image.name, image.content_type,
                      image.size, image.charset, image.content_type_extra]
        cache_key = 'image_key'
        cache.set(cache_key, image_data, 60)
        cache_data = cache.get(cache_key)
        image = InMemoryUploadedFile(*cache_data)
        AddPhotoModel(photos=image).save()
        return Response('上传图片文件成功!',status=status.HTTP_201_CREATED)


class AddHouseView(APIView):
    '''
    @brief :添加房源信息
    '''
    def post(self,request,*args,**kwargs):
        '''
        @brief:处理post请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        print('post data:')
        print(request.data)
        return Response('上传图片文件成功!',status=status.HTTP_201_CREATED) #201表示创建

    def get(self,request,*args,**kwargs):
        '''

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        print('get data:')
        print(request.data)
        return Response('处理get请求',status=status.HTTP_200_OK)