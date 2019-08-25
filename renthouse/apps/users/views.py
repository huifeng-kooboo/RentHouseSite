from .models import UserModel
from rest_framework import viewsets
from .serializers import UserSerializer

class UserLoginViewSet(viewsets.ModelViewSet):
    """
    @description: a basic function for userlogin
    @author: ytouch
    @email: gisdoing@gmail.com
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer