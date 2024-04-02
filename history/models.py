from django.db import models
from customer.models import customer
from django.db import models
from hotels.models import Hotel
# class Booking(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     customer = models.ForeignKey(customer, on_delete=models.CASCADE)
#     hotel_name = models.CharField(max_length=250)
#     image = models.ImageField(upload_to='history/image')
#     rooms = models.IntegerField()
#     total_cost = models.IntegerField()
class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    rooms = models.IntegerField()
    def __str__(self):
        return f"{self.customer.user.first_name} {self.customer.user.last_name}"




# class Buying(models.Model):
#     customer = models.ForeignKey(customer, on_delete=models.CASCADE)

#     rooms = models.IntegerField(default=0)

#     def __str__(self):
#         return f"customer : {self.customer.user.last_name}, hotel : {self.hotel.hotel_name}"