from django.contrib import admin
from . import models
# Register your models here.

class catagoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}

admin.site.register(models.category, catagoryadmin)
admin.site.register(models.Hotel)
admin.site.register(models.Review)