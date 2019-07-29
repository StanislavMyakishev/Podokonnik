from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ad, Category, Author
from .serializers import AdSerializer, CategorySerializer, UserSerializer

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")

class AdView(ListCreateAPIView):
    model = Ad
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('category__name', 'author')


class SingleAdView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class CategoryView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('name',)

class SingleCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer