from django.contrib import admin
from .models import Hotel, Department, EmployeeType, Employee


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by name
    list_filter = ('availability',)  # Add filters for availability

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'employee_type', 'email')
    list_filter = ('department', 'employee_type')
    search_fields = ('first_name', 'last_name', 'email')






# Register your models here.
