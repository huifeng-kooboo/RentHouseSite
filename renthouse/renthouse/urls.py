'''renthouse URL Configuration'''

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

#@comment: data view
from users.views import UserLoginViewSet,UserRegisterViewSet
from users.logic_views import LoginView,RegisterView

router = DefaultRouter()
router.register(r'test',UserLoginViewSet) #用户登录模块
#router.register(r'logintest',LoginView)
router.register(r'registertest',UserRegisterViewSet)


urlpatterns = [
    url(r'^login/',LoginView.as_view(),name='login'), #@comment: login page
    url(r'^register/',RegisterView.as_view(),name= 'register'), #@comment: register page
    path('api-token-auth/',views.obtain_auth_token),
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
