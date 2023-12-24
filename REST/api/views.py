from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from.serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework .decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Employee
from .serializers import UserSerializer


@api_view(['GET','POST'])
def Employeelistview(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE','GET','PUT'])
def employeeDetailview(request,pk):
    try:
        employee = Employee.objects.get(pk=pk) 
    except Employee.DoesNotExist:
        return Response(status=404)
    
    if request.method =='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET'])    
def Userlistview(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)