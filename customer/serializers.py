from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from .models import customer

class customerSrializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.customer
        fields = '__all__'

class RegistrationSrializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    mobile_no = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email','mobile_no','password', 'confirm_password',]

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        mobile_no = self.validated_data.get('mobile_no')



        if password != password2:
            raise serializers.ValidationError({'error': "password Doesn't matched"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        customer.objects.create(
            user = account,
            mobile_no = mobile_no,
            balance = 0,
        )
        return account
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required = True)      