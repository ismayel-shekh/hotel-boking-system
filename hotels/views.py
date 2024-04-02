from django.shortcuts import render
from rest_framework import fields, pagination
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters
from django.shortcuts import redirect

class catagorywoyshotel(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        hotel_id = request.query_params.get('hotel_id')
        if hotel_id:
            return query_set.filter(hotel = hotel_id)
        return query_set

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.catagorySerializer
    # filter_backends = [catagorywoyshotel]

class HotelPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class HotelViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer
    filter_backends = [filters.SearchFilter]
    # pagination_class = HotelPagination
    search_fields = ['hotel_name', 'category__name']



class revieshotel(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        hotel_id = request.query_params.get("hotel_id")
        if hotel_id == 'null':
            return query_set.none()
        if hotel_id:
            return query_set.filter(hotel = hotel_id)
        return query_set

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [revieshotel]