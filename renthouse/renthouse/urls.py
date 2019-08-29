'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken import views
from django.views.generic.base import TemplateView

import xadmin

#@comment: data view
from users.views import UserRegisterViewSet,LoginView

router = DefaultRouter()
router.register(r'register',UserRegisterViewSet,base_name='register') #用户注册


urlpatterns = [
   # url(r'^login/',LoginView.as_view(),name='login'), #用户登录
    path('api-token-auth/',views.obtain_auth_token),
    #path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
   # url(r'^',include(router.urls)),
    path(r'', TemplateView.as_view(template_name="index.html")),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
