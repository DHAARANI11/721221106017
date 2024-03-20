from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

class UserSerializer(serializer.ModelSerializer):

    class Meta:
        model=User
        field='__all__'

class ProductSerializer(serializer.ModelSerializer):

    class Meta:
        model=Productfield='__all__'