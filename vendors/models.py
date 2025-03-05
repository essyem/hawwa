from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    room_types = models.JSONField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)  # E.g., Operations, HR, IT
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name

class EmployeeType(models.Model):
    name = models.CharField(max_length=200, unique=True)  # E.g., Permanent, Contract, Temp

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Link to Department
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)  # Link to EmployeeType
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
