# vendors/views.py
from rest_framework import viewsets
from .models import Hotel, NursingProvider, CloudKitchen
from .serializers import HotelSerializer, NursingProviderSerializer, CloudKitchenSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class NursingProviderViewSet(viewsets.ModelViewSet):
    queryset = NursingProvider.objects.all()
    serializer_class = NursingProviderSerializer

class CloudKitchenViewSet(viewsets.ModelViewSet):
    queryset = CloudKitchen.objects.all()
    serializer_class = CloudKitchenSerializer
