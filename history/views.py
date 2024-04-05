from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# class bookingViewset(viewsets.ModelViewSet):
#     queryset = models.Booking.objects.all()
#     serializer_class = serializers.historySerialializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         customer_id = self.request.query_params.get('customer_id')
#         if customer_id:
#             queryset = queryset.filter(customer_id=customer_id)
#         return queryset


# class bokingviewset(viewsets.ModelViewSet):
#     queryset = models.Buying.objects.all()
#     serializer_class = serializers.BookingSerializer
### demo code ###

from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models
from . import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User

class BookingViewset(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        print("hellow bro")
        # print(self.request.query_parms)
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset

    def create(self, request, *args, **kwargs):

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        customer_id = request.data.get('customer')
        # customerx = models.customer.objects.get(id=customer_id)
        print(customer_id)
        hotel_id = request.data.get('hotel')
        rooms = request.data.get('rooms')
        rooms = int(rooms)
        current_user = User.objects.get(id=customer_id)
        print("line53",current_user.email)
        # print(current_user.first_name)
        current_customer = models.customer.objects.get(user=current_user)
        print(current_customer.id)
        print(current_customer.balance)

        # print(customer.user.first_name)
        # print(customer.balance)
        print(hotel_id)
        hotel = models.Hotel.objects.get(id=hotel_id)

        total_cost = hotel.room_price * rooms
        if hotel.avilable_room >= rooms:
            print(hotel.avilable_room)
            if current_customer.balance >= total_cost:
                # serializer.save()
                current_customer.balance -= total_cost
                current_customer.save()
                hotel.avilable_room -= rooms
                hotel.save()
                print("booking")
                x = models.Booking.objects.create(
                    hotel = hotel,
                    customer = customerx,
                    rooms = rooms,
                )
                x.save()
                email_subject = "hotel room booking succesfully"
                email_body = render_to_string('booking.html',{'user': current_customer.user, 'hotel': hotel, 'room':rooms, 'total':total_cost, 'balance': current_customer.balance})
                email = EmailMultiAlternatives(email_subject,'', to=[current_customer.user.email])
                email.attach_alternative(email_body, "text/html")
                email.send()
                return Response({"message": "Booking successful Chack your email"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Not Available rooms"}, status=status.HTTP_400_BAD_REQUEST)


