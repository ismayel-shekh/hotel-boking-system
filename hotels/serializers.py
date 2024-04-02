from rest_framework import serializers
from . import models

class HotelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Hotel
        fields = '__all__'

class catagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # reviewer = serializers.StringRelatedField(many=False)
    # hotel = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Review
        fields = '__all__'
        