from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer
from django.http import JsonResponse

def vendor_list(request):
    return JsonResponse({"message": "Vendor list endpoint"})

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
# Create your views here.
