from django.urls import path
from .views import index ,Dashboard ,handle_login

urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'), 
    path('', index, name='index'),
    path('handle_login/', handle_login, name='handle-login'),
]