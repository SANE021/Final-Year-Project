from django.urls import path
from . import views

urlpatterns = [
    path('', views.songs_list, name='songs-list'),
    path('detail/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    
]