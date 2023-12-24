from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User


## Models Serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'







# class EmployeeSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=50)
    # email =serializers.EmailField()
    # password = serializers.CharField(max_length=50)
    # phone = serializers.CharField(max_length=20)


    
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     newEmployee = Employee(**validated_data)
    #     newEmployee.save()
    #     return newEmployee

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     email =serializers.EmailField()
#     password = serializers.CharField(max_length=50)
    
