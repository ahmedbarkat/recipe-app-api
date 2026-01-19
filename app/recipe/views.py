from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication, permissions 
from rest_framework_simplejwt.authentication import JWTAuthentication 
from recipe.serializers import (RecipeDetailSeralizer, RecipeSerializer)
from core.models import Reciepe
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication, JWTAuthentication]
    permission_classes =  [permissions.IsAuthenticated]

    serializer_class = RecipeDetailSeralizer
    queryset = Reciepe.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeSerializer
        return self.serializer_class    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)