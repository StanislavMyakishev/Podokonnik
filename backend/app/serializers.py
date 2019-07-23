from django.utils import timezone
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Ad, Category, Author

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'descr', 'date', 'price', 'category', 'author', 'favorite_for']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name',]

    def create(self, validated_data):
        user = User(**validated_data)
        user.username = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()
        return user