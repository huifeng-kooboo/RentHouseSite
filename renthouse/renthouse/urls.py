'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken import views
from django.views.generic.base import TemplateView

from renthouse.settings import MEDIA_ROOT

import xadmin

from django.views.static import serve

#@comment: data view
from users.views import UserRegisterViewSet,LoginView,AddHouseView,AddPhotoView

router = DefaultRouter()
router.register(r'register',UserRegisterViewSet,base_name='register') #用户注册
#router.register(r'addhouse',AddHouseInfoViewSet,base_name='addhouse')
#router.register(r'addphoto',AddPhotoViewSet,base_name='addphoto')

urlpatterns = [
    url(r'^addhouse/',AddHouseView.as_view(),name='addhouse'),# 添加房源请求
    url(r'^login/',LoginView.as_view(),name='login'), #用户登录
    url(r'^addphoto/',AddPhotoView.as_view(),name='addphoto'), #保存所有上传的图片资源
    path('api-token-auth/',views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    url(r'media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
   #
    path(r'', TemplateView.as_view(template_name="index.html")), #绑定前端，相当于与前端进行交互
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
