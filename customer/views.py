from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
# for emalil
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class customerViewset(viewsets.ModelViewSet):
    queryset = models.customer.objects.all()
    serializer_class = serializers.customerSrializer

class USERViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.USERSrializer
    

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSrializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://hotel-boking-system.onrender.com/user/active/{uid}/{token}"
            
            email_subject = "Active your Account"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({'success':"Check your mail for confirmation"})
        return Response(serializer.errors)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(user.id)
        print(user.pk)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('http://127.0.0.1:5501/login.html')
    else:
        return redirect('register')
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                print(user.id)

                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors) 
    
class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        # logout(request)
        return redirect('login')

# from rest_framework.generics import GenericAPIView 
# class UserLogoutView(GenericAPIView):
#     def get(self, request, format=None):
#         if request.is_authenticated():
#             request.user.auth_token.delete()
#         return redirect('login')