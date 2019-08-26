from .models import UserModel
from rest_framework import viewsets,mixins
from .serializers import UserSerializer

class UserLoginViewSet(viewsets.ModelViewSet):
    """
    @description: a basic function for userlogin
    @author: ytouch
    @email: gisdoing@gmail.com
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRegisterViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
