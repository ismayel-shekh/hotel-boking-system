from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
class historyViewset(viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    serializer_class = serializers.historySerialializer