from rest_framework import serializers
from . import models
class historySerialializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = '__all__'