"""products models"""
from django.db import models

class Products (models.Model):
    product_name=models.CharField(max_length=20,blank=True)
    provider=models.ForeignKey( 'providers.Providers', on_delete=models.CASCADE)
    existing_units=models.CharField(max_length=11,blank=True)
    date_entry=models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=20)