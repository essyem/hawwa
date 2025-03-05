from django.urls import path
from .views import generate_ai_module

urlpatterns = [
    path('generate-ai-module/', generate_ai_module, name='generate_ai_module'),
]

#from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.wellness_programs, name='wellness_programs'),
]
#wellness yoga

