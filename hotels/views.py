from django.shortcuts import render
from rest_framework import fields, pagination
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.catagorySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer
    search_fields = ['category']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer