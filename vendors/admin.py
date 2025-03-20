# vendors/admin.py
from django.contrib import admin
from .models import Hotel, NursingProvider, Department, EmployeeType, Employee, CloudKitchen

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability')
    search_fields = ('name',)
    list_filter = ('availability',)

@admin.register(NursingProvider)
class NursingProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'certifications')
    search_fields = ('name', 'certifications')
    list_filter = ('certifications',)

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
    list_display = ('first_name', 'last_name', 'department', 'employee_type', 'email', 'phone', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('department', 'employee_type', 'hire_date')
    list_select_related = ('department', 'employee_type')
    date_hierarchy = 'hire_date'

@admin.register(CloudKitchen)
class CloudKitchenAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine_type', 'location', 'is_active')
    search_fields = ('name', 'cuisine_type', 'location')
    list_filter = ('is_active', 'cuisine_type')
