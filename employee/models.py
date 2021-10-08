"""employee models"""
from django.db import models

class Employees(models.Model):
    """Atributte"""
    first_name=models.CharField(max_length=20,blank=True)
    last_name=models.CharField(max_length=20,blank=True)

    phone_number=models.CharField(max_length=11,blank=True)
    is_admin=models.BooleanField()

