from django.db import models
from django.contrib import admin

# Create your models here.
class Cars (models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    year = models.DateField()
    price = models.IntegerField()
    type = models.CharField(max_length=50)

class Car (admin.ModelAdmin):
    list_display = ('id','brand','model','year','price','type')






