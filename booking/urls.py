from django.urls import path
from .views import Service ,Booked

urlpatterns = [
    path('service/', Service, name='services'),
    path('booked/', Booked, name='booked'),
    
]