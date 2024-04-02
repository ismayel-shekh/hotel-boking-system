from rest_framework import serializers
from . import models
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = '__all__'

# from rest_framework import serializers
# from . import models

# class DepositSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Deposit
#         fields = ['deposit'] 

#     def create(self, validated_data):

#         validated_data['customer'] = self.context['request'].user.customer
#         return super().create(validated_data)

# from rest_framework import serializers
# from . import models

# class DepositSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Deposit
#         fields = ['deposit'] 

#     def create(self, validated_data):

#         validated_data['customer'] = self.context['request'].user.customer
#         return super().create(validated_data)