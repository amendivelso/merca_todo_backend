from rest_framework import serializers
from management.models import Tutorial

class ManagementSerializers(serializers.ModelSerializer):
  class Meta:
    model=Tutorial
    fields=(
      'id',
      'title',
      'description',
      'published',
    )