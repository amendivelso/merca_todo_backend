from rest_framework import serializers
from employee.models import Employees

class EmployeesSerializers(serializers.ModelSerializer):
  class Meta:
    model=Employees
    fields=(
      'first_name',
      'last_name',
      'phone_number',
      'is_admin',
    )