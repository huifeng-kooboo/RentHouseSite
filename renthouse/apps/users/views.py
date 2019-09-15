from rest_framework import viewsets,mixins
from .models import UserModel,HouseInfoModel,AddPhotoModel,LandlordManage
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,HouseInfoSerializer,BriefHouseInfoSerializer,RenterBriefInfoSerializer,LandloadManageSerializer
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

class BriefHouseInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief: 主页房源信息展示功能
    '''
    queryset = HouseInfoModel.objects.all()
    serializer_class = BriefHouseInfoSerializer #get请求返回的数据

class HouseDetailInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief: 获得单个房源所有信息功能
    '''
   # queryset = HouseInfoModel.objects.all()
    serializer_class = HouseInfoSerializer
    def get_queryset(self):
        '''
        @brief:设置过滤条件
        '''
        print('see')
        send_params = self.request.query_params
        cur_title = send_params['house_title']
        print(cur_title)
        #进行过滤
        return HouseInfoModel.objects.filter(house_title = cur_title)

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
        image = request.data['file']
        image_data = [image.file, image.field_name, image.name, image.content_type,
                      image.size, image.charset, image.content_type_extra]
        cache_key = 'image_key'
        cache.set(cache_key, image_data, 60)
        cache_data = cache.get(cache_key)
        cur_image = InMemoryUploadedFile(*cache_data)
        cur_house_title = request.data['house_title']
        cur_basic_interviews = request.data['basic_interviews']
        cur_house_price = request.data['house_price']
        cur_house_position = request.data['house_position']
        cur_connect_phone = request.data['connect_phone']
        cur_renter_name = request.data['renter_name']
        lendata = HouseInfoModel.objects.filter(house_title=cur_house_title)
        # 格式信息 由前端进行判断 后端暂时不去判断
        if len(lendata) == 1:
            return Response('上传失败',status=status.HTTP_200_OK) #返回给前端
        HouseInfoModel(house_images=cur_image,house_title=cur_house_title,basic_interviews=cur_basic_interviews,house_price=cur_house_price,
                       house_position=cur_house_position,connect_phone=cur_connect_phone,renter_name=cur_renter_name).save()
        return Response('添加成功!',status=status.HTTP_201_CREATED) #201表示创建

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

class RenterBriefInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief:租户管理中使用
    '''
    serializer_class = RenterBriefInfoSerializer
    def get_queryset(self):
        '''
        @brief:设置过滤条件
        '''
        #逻辑： 默认情况下，非管理员 is_admin = False 则为租户
        return UserModel.objects.filter(is_admin=False)

class LandloadManageViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    @brief:创建租户管理类
    '''
    queryset = LandlordManage.objects.all()
    serializer_class = LandloadManageSerializer
