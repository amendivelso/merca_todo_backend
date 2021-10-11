"""models provider"""
from django.db import models

# Create your models here.
class Providers (models.Model):
    
    address = models.CharField("Address",max_length=100,)
    units_shipping=models.CharField(max_length=11)
    
    phone_number=models.CharField(max_length=11)
    is_admin=models.BooleanField(blank=False)
