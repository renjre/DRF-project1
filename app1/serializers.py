from pyexpat import model
from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.IntegerField()
    employee_id = serializers.IntegerField()

    def create(self, validated_data):
        print("called create method")
        return Employee.objects.create(**validated_data)

    def update(self, employee, validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id = employee.id
        newEmployee.save()
        return newEmployee