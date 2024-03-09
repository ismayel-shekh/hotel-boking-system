from django.db import models
from customer.models import customer
class History(models.Model):
    image = models.ImageField(upload_to='history/image')
    hotel_name = models.CharField(max_length=250)
    rooms = models.IntegerField()
    total_cost = models.IntegerField()
    user = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"