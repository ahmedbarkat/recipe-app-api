from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate
 
from core.models import User
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "name"]
        extra_kwargs = {"password":{"write_only":True},"mine_length":5}
        def create(self,validate_data):
            return get_user_model().objects.create_user(**validate_data)
        def update(self, instance, validate_data):
            password = validate_data.pop('password')
            user = super().update(instance,**validate_data)
            if password:
                user.set_password(password)
                user.save()
            return user        


     
class UserToken(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type':'password'},required=True, trim_whitespace=False)
 
    def validate(self, attrs):
        email = attrs.get('email',None)
        password = attrs.get('password', None)
        if not email or not password:
            raise serializers.ValidationError('Please Check credential',code='credential')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
 
        if not user:
            msg = ('Unble to authenticate with provide credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        return attrs    

