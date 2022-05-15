from django.contrib import admin
from django.urls import path
from .views import EmployeeListView, UserListView, EmployeeDetailView
urlpatterns = [
    path('employees/', EmployeeListView),
    path('employee/<int:pk>', EmployeeDetailView),
    path('users/', UserListView),
]