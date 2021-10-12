
from rest_framework import serializers
from products.models import Products

class ProductsSerializers(serializers.ModelSerializer):
  class Meta:
    model=Products
    fields=(
      'id',
      'product_name',
      'provider',
      'existing_units',
      'date_entry',
      'description',
      'category'
    )