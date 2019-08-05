from django.utils import timezone
from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                           get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.db import models

from django.utils.translation import ugettext_lazy as _
from rest_auth.registration.serializers import RegisterSerializer

from .models import Ad, Category, Author

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'descr', 'date', 'price', 'category', 'author', 'favorite_for']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RegisterSerializer(RegisterSerializer):
    room = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=14)
    first_name = serializers.CharField(max_length=14)
    last_name = serializers.CharField(max_length=14)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.room = self.cleaned_data['room']
        user.save(update_fields=['phone', 'room'])

    def get_cleaned_data(self):
        with open('file.txt', 'w') as f:
            f.write(str(self.validated_data) + "\n")
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'room': self.validated_data.get('room', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user