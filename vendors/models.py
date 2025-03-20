# vendors/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    room_types = models.JSONField()
    availability = models.BooleanField(default=True)
    amenities_inclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class NursingProvider(models.Model):
    name = models.CharField(max_length=200)
    certifications = models.TextField()
    languages = models.JSONField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class EmployeeType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CloudKitchen(models.Model):
    name = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=100)  # E.g., Italian, Indian, etc.
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
