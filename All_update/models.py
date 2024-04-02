from django.db import models
from customer.models import customer
# Create your models here.
class Deposit(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    deposit = models.IntegerField()
    