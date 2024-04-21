from django import views
from django.urls import path
from .views import create_artist_profile,upload_song, edit_song, delete_song,ArtistProfileView, EditProfileView 


urlpatterns = [
        path('create-artist-profile/', create_artist_profile, name='create_artist_profile'),
        path('upload-song/', upload_song, name='upload_song'),
        path('edit-song/<int:song_id>/', edit_song, name='edit_song'),
        path('delete-song/<int:song_id>/', delete_song, name='delete_song'),
        path('profile/', ArtistProfileView.as_view(), name='artist_profile'),
        path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
        
]