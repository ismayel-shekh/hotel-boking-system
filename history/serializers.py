from rest_framework import serializers
from . import models
class BookingSerializer(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField(many=False)
    # hotel = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Booking
        fields = '__all__'

    # def create(self, validated_data):

    #     validated_data['customer'] = self.context['request'].user.customer
    #     return super().create(validated_data)

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Buying
#         fields = '__all__'
        

