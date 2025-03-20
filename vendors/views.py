# vendors/views.py
from rest_framework import viewsets
from .models import Hotel, NursingProvider, Department, EmployeeType, Employee, CloudKitchen
from .serializers import HotelSerializer, NursingProviderSerializer, DepartmentSerializer, EmployeeTypeSerializer, EmployeeSerializer, CloudKitchenSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class NursingProviderViewSet(viewsets.ModelViewSet):
    queryset = NursingProvider.objects.all()
    serializer_class = NursingProviderSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CloudKitchenViewSet(viewsets.ModelViewSet):
    queryset = CloudKitchen.objects.all()
    serializer_class = CloudKitchenSerializer
