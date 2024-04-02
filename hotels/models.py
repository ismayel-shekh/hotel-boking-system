from django.db import models
from customer.models import customer

class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    category = models.ManyToManyField(category)
    hotel_name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    details = models.TextField()
    card_image = models.ImageField(upload_to='hotels/image/')
    image_1 = models.ImageField(upload_to='hotels/image/')
    image_2 = models.ImageField(upload_to='hotels/image/')
    avilable_room = models.IntegerField(default=0)
    room_price = models.IntegerField()
    def __str__(self):
        return self.hotel_name


STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),

]

class Review(models.Model):
    name = models.CharField(max_length=250)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = STAR_CHOICES, max_length=10)
    def __str__(self):
        return self.name