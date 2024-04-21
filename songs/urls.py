from django.urls import path
from . import views 
from .views import MySongsView

urlpatterns = [
    path('', views.songs_list, name='songs-list'),
    path('my-songs/', MySongsView.as_view(), name='my_songs'),
    path('detail/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    
]