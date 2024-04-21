from django.urls import path
from .views import Service ,Booked ,verify_payment,khalti_payment

urlpatterns = [
    path('service/', Service, name='services'),
    path('booked/', Booked, name='booked'),
    path('khakti-payment/', khalti_payment,name='khalti_payment'),
    path('api/verify_payment',verify_payment,name='verify_payment')
    
]