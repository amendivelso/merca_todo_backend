#django
from django.shortcuts import render
from django.http.response import JsonResponse
#rest_framework
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
#employees models
from employee.models import Employees
from employee.serializers import EmployeesSerializers

@api_view(['GET', 'POST', 'DELETE'])
def employees_list(request):
    if request.method == 'GET':
        tutorials = Employees.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = EmployeesSerializers(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = EmployeesSerializers(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Employees.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try: 
        tutorial = Employees.objects.get(pk=pk) 
    except Employees.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = EmployeesSerializers(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer =EmployeesSerializers(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        


@api_view(['GET'])
def employees_list_admin(request):
    employees = Employees.objects.filter(is_admin=1)
        
    if request.method == 'GET': 
        employees_serializer = EmployeesSerializers(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
@api_view(['GET'])
def employees_list_user(request):
    employees = Employees.objects.filter(is_admin=0)
        
    if request.method == 'GET': 
        employees_serializer = EmployeesSerializers(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)