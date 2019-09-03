'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken import views
from django.views.generic.base import TemplateView

import xadmin

#@comment: data view
from users.views import UserRegisterViewSet,LoginView,AddHouseInfoViewSet

router = DefaultRouter()
router.register(r'register',UserRegisterViewSet,base_name='register') #用户注册
router.register(r'addhouse',AddHouseInfoViewSet,base_name='addhouse')

urlpatterns = [
    url(r'^login/',LoginView.as_view(),name='login'), #用户登录
    path('api-token-auth/',views.obtain_auth_token),
    #path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
   #
    path(r'', TemplateView.as_view(template_name="index.html")), #绑定前端，相当于与前端进行交互
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
