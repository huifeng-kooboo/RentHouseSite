'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken import views
from django.views.generic.base import TemplateView
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token
from renthouse.settings import MEDIA_ROOT

import xadmin

from django.views.static import serve

#@comment: data view
from users.views import UserRegisterViewSet,LoginView,AddHouseView,AddPhotoView,BriefHouseInfoViewSet,HouseDetailInfoViewSet,RenterBriefInfoViewSet,LandloadManageViewSet,FeelistViewSet,AnalysisToken,MyInfoViewSet,AdViewSet,AllRenterHouseViewSet

router = DefaultRouter()
router.register(r'register',UserRegisterViewSet,base_name='register') #用户注册
router.register(r'briefhouseinfo',BriefHouseInfoViewSet,base_name='briefhouseinfo') # 简单的主页信息展示
router.register(r'housedetail',HouseDetailInfoViewSet,base_name='housedetail') #获取单个房源所有信息
router.register(r'briefuser',RenterBriefInfoViewSet,base_name='briefuser') # 显示所有租户的信息：备注：只能通过get请求
router.register(r'addland',LandloadManageViewSet,base_name='addland') #添加到租户管理部分 只处理post请求
router.register(r'feelist',FeelistViewSet,base_name='feelist')#费用清单
router.register(r'myinfo',MyInfoViewSet,base_name='myinfo') #个人信息设置部分 get获取数据 更新数据
router.register(r'ads',AdViewSet,base_name='ad') #首页走马车的广告栏
router.register(r'allrenters',AllRenterHouseViewSet,base_name='allrenters') #获取所有房源信息，展示到前端房源管理部分

urlpatterns = [
    url(r'^gettoken/', obtain_jwt_token), #登录获取token
    url(r'^addhouse/',AddHouseView.as_view(),name='addhouse'),# 添加房源请求
    url(r'^login/',LoginView.as_view(),name='login'), #用户登录
    url(r'^addphoto/',AddPhotoView.as_view(),name='addphoto'), #保存所有上传的图片资源

    #解析token类
    url(r'^anatoken/',AnalysisToken.as_view(),name='anatoken'),

    path('api-token-auth/',views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    url(r'media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),

    path(r'', TemplateView.as_view(template_name="index.html")), #绑定前端，相当于与前端进行交互
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
