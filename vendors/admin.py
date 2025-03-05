from django.contrib import admin
from .models import Hotel



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by name
    list_filter = ('availability',)  # Add filters for availability

# Register your models here.
