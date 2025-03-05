from django.urls import path
from .views import HotelListCreateView
from . import views

urlpatterns = [
    path('', views.vendor_list, name='vendor-list'),
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
]
