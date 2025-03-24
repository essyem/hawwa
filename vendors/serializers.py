# vendors/serializers.py
from rest_framework import serializers
from .models import Hotel, NursingProvider, CloudKitchen

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class NursingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursingProvider
        fields = '__all__'

class CloudKitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model =CloudKitchen
        fields = '__all__'
