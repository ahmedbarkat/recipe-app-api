from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication, permissions
from rest_framework.settings import  api_settings
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import (UserSerializer, UserToken)
# Create your views here.
class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer




class CreateUserToken(ObtainAuthToken):
    serializer_class = UserToken
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
     

class ManageUserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, JWTAuthentication]
    permission_classes =  [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
    

