from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
def UserListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False )

@csrf_exempt
def EmployeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # import pdb;pdb.set_trace()
        jsondata = JSONParser().parse(request)
        print(jsondata)
        serializer = EmployeeSerializer(data = jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)

@csrf_exempt
def EmployeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
    if request.method=="DELETE":
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    if request.method=="PUT":
        jsondata = JSONParser().parse(request)
        print(jsondata)
        serializer = EmployeeSerializer(employee, data = jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)