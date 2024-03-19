from django.db import models
from django.contrib.auth.models import User
class customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    