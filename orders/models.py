"""models order"""
from django.db import models

# Create your models here.


class Head_orders (models.Model):
    
    name_client= models.CharField(default="Mercatodo", max_length=11)
    address = models.CharField(default="Address",max_length=100) 
    dispatch_date=models.DateTimeField(auto_now_add=True)  

class Body_orders (models.Model):
    product=models.ForeignKey('products.Products',on_delete=models.CASCADE)    

class Orders (models.Model):
    

    body_order=models.OneToOneField(Body_orders,on_delete=models.CASCADE)
    head_order=models.OneToOneField(Head_orders, on_delete=models.CASCADE)