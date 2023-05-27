from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'dob', 'password')
        extra_kwargs = {'password': {'write_only': True}}

