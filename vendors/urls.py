# vendors/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, NursingProviderViewSet, DepartmentViewSet, EmployeeTypeViewSet, EmployeeViewSet, CloudKitchenViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'nursing-providers', NursingProviderViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employee-types', EmployeeTypeViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'cloudkitchen', CloudKitchenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
