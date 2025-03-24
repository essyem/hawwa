# vendors/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, NursingProviderViewSet, CloudKitchenViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'nursing-providers', NursingProviderViewSet)
router.register(r'cloudkitchen', CloudKitchenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
