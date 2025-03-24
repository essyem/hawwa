# vendors/admin.py
from django.contrib import admin
from .models import Hotel, NursingProvider, CloudKitchen

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

@admin.register(CloudKitchen)
class CloudKitchenAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine_type', 'location', 'is_active')
    search_fields = ('name', 'cuisine_type', 'location')
    list_filter = ('is_active', 'cuisine_type')
