from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from allauth.account.adapter import get_adapter

from .models import Ad, Category, Author
from .serializers import AdSerializer, CategorySerializer

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")

class AdView(LoggingMixin, ListCreateAPIView):
    model = Ad
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('category__name', 'author')


class SingleAdView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class CategoryView(LoggingMixin, ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('name',)

class SingleCategoryView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
