from rest_framework import viewsets,mixins,generics
from .models import UserModel,HouseInfoModel,AddPhotoModel,LandlordManage,AdInfoModel
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,HouseInfoSerializer,BriefHouseInfoSerializer,RenterBriefInfoSerializer,LandloadManageSerializer,FeeListSerializer,MyInfoSerializer,AdPhotoSerializer
from .basic_tools import checkUserLoginInfo,checkSecurityPassword
from .signals import user_save
import json
from django.core.cache import cache
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_jwt.utils import jwt_decode_handler
from jwt.exceptions import DecodeError,ExpiredSignatureError

class UserRegisterViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    @description:用户注册功能
    '''
    authentication_classes = ()
    permission_classes = ()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class BriefHouseInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief: 主页房源信息展示功能
    '''
    # is_staff字段对应管理员权限
    authentication_classes = ()
    permission_classes = () # 这个表示所有权限
    queryset = HouseInfoModel.objects.all()
    serializer_class = BriefHouseInfoSerializer #get请求返回的数据

class HouseDetailInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief: 获得单个房源所有信息功能
    '''
    authentication_classes = ()
    permission_classes = () #所有都可以访问
    serializer_class = HouseInfoSerializer
    def get_queryset(self):
        '''
        @brief:设置过滤条件
        '''
        send_params = self.request.query_params
        cur_title = send_params['house_title']
        #进行过滤
        return HouseInfoModel.objects.filter(house_title = cur_title)

class LoginView(APIView):
    '''
    @description: a basic method to console login page
    @author: ytouch
    '''
    permission_classes = ()
    authentication_classes = ()
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
    @brief: 上传单张图片功能
    @author: ytouch
    '''
    #authentication_classes = ()
    permission_classes = [IsAdminUser] #只限制管理员可以访问
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
    permission_classes = [IsAdminUser] # 管理员
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
    @brief:租户管理中使用:显示租户姓名
    '''
    permission_classes = [IsAdminUser] #管理员权限
    serializer_class = RenterBriefInfoSerializer
    def get_queryset(self):
        '''
        @brief:设置过滤条件
        '''
        #逻辑： 默认情况下，非管理员 is_admin = False 则为租户
        return UserModel.objects.filter(is_staff=False) #非管理员均为租户

class LandloadManageViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    @brief:创建租户管理类
    '''
    permission_classes = [IsAdminUser] #只展示给管理员
    queryset = LandlordManage.objects.all()
    serializer_class = LandloadManageSerializer

class FeelistViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief:费用清单展示get请求
    '''
    permission_classes = [IsAuthenticated] #展示给租户 所以只要是登陆 都可以访问
    serializer_class = FeeListSerializer
    def get_queryset(self):
        '''
        @brief:设置过滤条件 get条件
        '''
        print(self.request.query_params)
        return LandlordManage.objects.filter(tenant=self.request.query_params['tenant'])#租户作为过滤条件

class AnalysisToken(APIView):
    '''
    @brief:解析Token字符串类，用于提取用户信息
    @remark:仅限所有已登录用户获取信息
    @url:'api/anatoken/'
    @return: 返回用户名和权限级别 ：1.游客权限 2.管理员权限 3.普通租户权限
    其中token为游客权限 说明已过期token或者token错误
    '''
    authentication_classes = ()
    permission_classes = () #允许所有用户使用
    def post(self,request,*args,**kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        token_value = request.data['token'] #获得前端传来的token值
        expired_response = {'username':'','permission':'visitor'} #过期数据返回该json
        #进行解析
        #捕获异常：有可能过期：
        try:
            user_dict = jwt_decode_handler(token=token_value)
        except DecodeError: #存在一个小bug 就是还有几个error没有判断
            #此处则说明过期或者无效
            return Response(expired_response,status=status.HTTP_200_OK)
        except ExpiredSignatureError:
            return Response(expired_response,status=status.HTTP_200_OK)
        else:
            print('进行接下来的步骤')
        if user_dict == None:
            return Response(expired_response,status=status.HTTP_200_OK)
        str_username = user_dict['username']
        print(str_username)
        record_Users = UserModel.objects.filter(username=str_username)
        is_Staff = record_Users[0].is_staff #获取是否为管理员
        res_data_admin = {'username': user_dict['username'], 'permission': 'admin'}
        res_data = {'username': user_dict['username'], 'permission': 'normal'}
        if is_Staff == True:
            return Response(res_data_admin,status = status.HTTP_200_OK)
        return Response(res_data,status=status.HTTP_200_OK)

class MyInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief:提供给前端个人信息,并允许用户进行更新操作,前端使用put方法 实现更新
    '''
    permission_classes = [IsAuthenticated] #对于所有用户都开放
    serializer_class = MyInfoSerializer
    def get_queryset(self):
        '''
        @brief: get请求，只需要一个用户名就行
        '''
        return UserModel.objects.filter(username=self.request.query_params['username'])
    def put(self,request):
        '''
        @brief:修改更新数据
        '''
        str_username = request.data['username']
        str_address = request.data['rent_address']
        str_idcard = request.data['idcard']
        str_phone = request.data['phone_number']
        UserModel.objects.filter(username=str_username).update(rent_address=str_address,idcard=str_idcard,phone_number=str_phone)
        return Response('更新成功',status=status.HTTP_200_OK)

class AdViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    '''
    @brief:首页广告请求：使用get请求获取
    '''
    permission_classes = ()
    serializer_class = AdPhotoSerializer
    queryset = AdInfoModel.objects.all()
    def delete(self,request):
        '''
        @brief:删除广告图片功能
        '''
        print(request.data['id'])
        cur_count = AdInfoModel.objects.filter(id=request.data['id'])
        print(len(cur_count))
        AdInfoModel.objects.filter(id=request.data['id']).delete()
        return Response('图片删除成功',status=status.HTTP_200_OK) #删除图片功能（根据id删除比较方便）
    def put(self,request):
        '''
        @brief:添加广告图片功能
        '''
        print('get nowtjj')
        image = request.data['image_url']
        print(image.name)
        image_data = [image.file, image.field_name, image.name, image.content_type,
                      image.size, image.charset, image.content_type_extra]
        cache_key = 'image_key'
        cache.set(cache_key, image_data, 60)
        cache_data = cache.get(cache_key)
        str_house_images = InMemoryUploadedFile(*cache_data)
        print('进行是')
        AdInfoModel.objects.create(adphoto=str_house_images)
        return Response('图片增加成功',status=status.HTTP_201_CREATED)


class AllRenterHouseViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''
    @brief:所有租户房源集合：使用get请求获取
    @remark:权限仅限管理员（房东）
    '''
    permission_classes = [IsAdminUser]
    serializer_class = LandloadManageSerializer
    queryset = LandlordManage.objects.all() # 显示所有的

class GetRenterInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.DestroyModelMixin):
    '''
    @brief:根据租户名获取用户租房信息
    '''
    permission_classes = [IsAdminUser]
    serializer_class = LandloadManageSerializer
    def get_queryset(self):
        return LandlordManage.objects.filter(tenant=self.request.query_params['tenant']) #传递用户名即可
    def put(self,request):
        '''
        @brief:修改更新数据中使用
        '''
        str_tenant = request.data['tenant']
        str_rental_time = request.data['rental_time']
        str_rental_address = request.data['rental_address']
        str_rent_fee = request.data['rent_fee']
        str_water_fee = request.data['water_fee']
        str_electric_fee = request.data['electric_fee']
        str_is_net = request.data['is_net']
        str_net_fee = request.data['net_fee']
        str_key_num = request.data['key_num']
        str_is_air = request.data['is_air']
        str_is_washer = request.data['is_washer']
        LandlordManage.objects.filter(tenant=str_tenant).update(rental_time=str_rental_time,
                                                                rent_fee=str_rent_fee,
                                                                rental_address=str_rental_address,
                                                                water_fee=str_water_fee,
                                                                electric_fee=str_electric_fee,
                                                                is_net=str_is_net,
                                                                net_fee= str_net_fee,
                                                                key_num= str_key_num,
                                                                is_air=str_is_air,
                                                                is_washer=str_is_washer)
        return Response('更新成功',status=status.HTTP_200_OK)
    def delete(self, request):
        '''
        @brief:删除功能
        '''
        LandlordManage.objects.filter(tenant=request.data['tenant']).delete()
        return Response('删除成功',status=status.HTTP_200_OK)


class AllHouseInfoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    '''
    @brief 获取所有房源的序列化信息:使用get请求
    '''
    permission_classes = [IsAdminUser]#管理员才能管理调试
    serializer_class = HouseInfoSerializer
    queryset = HouseInfoModel.objects.all() #使用get请求时，传递所有集合
    def put(self,request):
        '''
        @brief:更新数据，修改
        '''
        if request.data['is_upload'] == '0':
            print('处理无图片功能')
            str_house_title = request.data['house_title']
            # image = request.data['house_images']
            # print(image.name)
            # image_data = [image.file, image.field_name, image.name, image.content_type,
            #               image.size, image.charset, image.content_type_extra]
            # cache_key = 'image_key'
            # cache.set(cache_key, image_data, 60)
            str_basic_interviews = request.data['basic_interviews']
            str_house_price = request.data['house_price']
            str_house_position = request.data['house_position']
            str_connect_phone = request.data['connect_phone']
            str_renter_name = request.data['renter_name']
            '''
            @brief:后续改动 bug：无法更新的问题
            '''
            HouseInfoModel.objects.filter(house_title=request.data['house_title']).update(basic_interviews=str_basic_interviews, house_price=str_house_price,
                                          house_position=str_house_position, connect_phone=str_connect_phone,
                                          renter_name=str_renter_name)  # 更新
            # HouseInfoModel.objects.create(
            #                               basic_interviews=str_basic_interviews, house_price=str_house_price,
            #                               house_position=str_house_position, connect_phone=str_connect_phone,
            #                               renter_name=str_renter_name)
            return Response('修改成功', status=status.HTTP_200_OK)  # 修改成功
        str_house_title = request.data['house_title']
        image = request.data['house_images']
        print(image.name)
        image_data = [image.file, image.field_name, image.name, image.content_type,
                      image.size, image.charset, image.content_type_extra]
        cache_key = 'image_key'
        cache.set(cache_key, image_data, 60)
        cache_data = cache.get(cache_key)
        str_house_images = InMemoryUploadedFile(*cache_data)
        print(type(str_house_images))
        str_basic_interviews = request.data['basic_interviews']
        str_house_price = request.data['house_price']
        str_house_position = request.data['house_position']
        str_connect_phone = request.data['connect_phone']
        str_renter_name = request.data['renter_name']
        '''
        @brief:后续改动 bug：无法更新的问题
        '''
        HouseInfoModel.objects.filter(house_title=request.data['house_title']).delete()#删除
        HouseInfoModel.objects.create(house_title=str_house_title,house_images=image,basic_interviews=str_basic_interviews,house_price=str_house_price,house_position=str_house_position,connect_phone=str_connect_phone,renter_name=str_renter_name)
        return Response('修改成功',status=status.HTTP_200_OK) #修改成功
    def delete(self,request):
        '''
        @brief:删除数据：bug：还未解决批量删除数据的问题：后面调整修复
        '''
        print(request.data)
        HouseInfoModel.objects.filter(house_title=request.data['house_title']).delete()
        return Response('数据删除成功！',status=status.HTTP_200_OK)