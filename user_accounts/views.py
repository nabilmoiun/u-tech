from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import generics
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    CustomAuthTokenSerializer
)


User = get_user_model()


class Login(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class RegisterUser(generics.CreateAPIView):
    """
    Registration Api
    Creates new user instance
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
