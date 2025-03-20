# vendors/serializers.py
from rest_framework import serializers
from .models import Hotel, NursingProvider, Department, EmployeeType, Employee, CloudKitchen

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class NursingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursingProvider
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CloudKitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model =CloudKitchen
        fields = '__all__'
