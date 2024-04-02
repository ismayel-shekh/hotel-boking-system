# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from . import models
# from . import serializers
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# # Create your views here.
# class DepositViewset(viewsets.ModelViewSet):
#     queryset = models.Deposit.objects.all()
#     serializer_class = serializers.DepositSerializer


#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         customer = request.user.customer
#         customer_id = request.data.get('customer')
#         print(customer_id)
#         deposit = int(request.data.get('deposit'))
#         customer = models.customer.objects.get(pk=customer_id)
#         serializer.save(customer=customer)
#         print(request.user.customer)
#         print(customer)
#         serializer.save
#         if deposit >= 0:
#             customer = request.user.customer
#             print(request.user.customer)
#             print(customer)
#             print(customer)
#             customer.balance += deposit
#             customer.save()
#             serializer.save(customer=customer)
#             email_subject = "Deposit  succesful"
#             email_body = render_to_string('deposit.html',{'user': customer.user, 'balance': customer.balance, 'money': deposit})
#             email = EmailMultiAlternatives(email_subject,'', to=[customer.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()
#             return Response({"message": "deposit Successfull Chack mail"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "balanace must be Positive"}, status=status.HTTP_400_BAD_REQUEST)

# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from . import models
# from . import serializers
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class DepositViewset(viewsets.ModelViewSet):
#     queryset = models.Deposit.objects.all()
#     serializer_class = serializers.DepositSerializer

#     def create(self, request, *args, **kwargs):

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(request)
#         # Assuming you have an authenticated user
#         current_customer = request.user.customer
#         print(current_customer)
#         cust = request.user.customer
#         print(self.request.user)
#         deposit = int(request.data.get('deposit'))

#         # Associate the deposit with the current user's customer
#         serializer.save(customer=current_customer)

#         if deposit >= 0:
#             cust.balance += deposit
#             cust.save()

#             email_subject = "Deposit successful"
#             email_body = render_to_string('deposit.html', {'user': cust.user, 'balance': cust.balance, 'money': deposit})
#             email = EmailMultiAlternatives(email_subject, '', to=[cust.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()

#             return Response({"message": "Deposit successful. Check email"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Balance must be positive"}, status=status.HTTP_400_BAD_REQUEST)

# orginal code

# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from . import models
# from . import serializers
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class DepositViewset(viewsets.ModelViewSet):
#     queryset = models.Deposit.objects.all()
#     serializer_class = serializers.DepositSerializer

#     def create(self, request, *args, **kwargs):

#         current_customer = request.user.customer

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)


#         serializer.save(customer=current_customer)

#         deposit = int(request.data.get('deposit'))

#         if deposit >= 0:

#             current_customer.balance += deposit
#             current_customer.save()

#             email_subject = "Deposit successful"
#             email_body = render_to_string('deposit.html', {'user': current_customer.user, 'balance': current_customer.balance, 'money': deposit})
#             email = EmailMultiAlternatives(email_subject, '', to=[current_customer.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()

#             return Response({"message": "Deposit successful. Check email"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Deposit amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)


# avishak vhi povided code

from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models
from . import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class DepositViewset(viewsets.ModelViewSet):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositSerializer
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # current_customer = request.user.customer
# error hear 
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(customer=current_customer)

        deposit = int(request.data.get('deposit'))
        customer_id = int(request.data.get('customer'))
        print(customer_id)
        current_user = User.objects.get(id=customer_id)
        print(current_user)
        print(current_user.first_name)
        x = models.customer.objects.get(user=current_user)
        print(x.id)
        print(x.user.first_name, x.user.last_name)
        # current_customer = current_user.user

        # current_customer = models.customer.objects.get(id=x)
        # print(current_customer)

        # current_customer = User.objects.get(id=customer_id)
        # print(current_customer)
        # c = models.customer.objects.get(user=current_customer)
        # print(c)
        # print(current_customer)
        # akhana User selo
        if deposit >= 0:
            x.balance += deposit
            x.save()

            # c.balance += deposit
            # c.save()

            email_subject = "Deposit successful"
            email_body = render_to_string(
                'deposit.html', {'user': x.user, 'balance': x.balance, 'money': deposit})
            email = EmailMultiAlternatives(
                email_subject, '', to=[x.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message": "Deposit successful. Check email"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Deposit amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)
