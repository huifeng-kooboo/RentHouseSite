'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

#@comment: data view
from users.views import UserLoginViewSet
from users.logic_views import LoginView

router = DefaultRouter()
#router.register(r'test',LoginView) #用户登录模块

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('api-token-auth/',views.obtain_auth_token),
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
