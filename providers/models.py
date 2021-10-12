"""models provider"""
from django.db import models

# Create your models here.
class Providers (models.Model):
    
    address = models.CharField("Address",max_length=100,blank=True)
    units_shipping=models.IntegerField(blank=True)
    
    phone_number=models.CharField(max_length=15,blank=True)
    is_admin=models.BooleanField(blank=True,default=0)
