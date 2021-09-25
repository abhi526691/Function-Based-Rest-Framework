from django.db import models
from rest_framework import fields, serializers
from .models import MyData, User

class MyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyData
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

