from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('songName', 'genre', 'song', 'artist')  # Add 'artist' to the list display

    def artist(self, obj):
        return obj.artist.username if obj.artist else None

    artist.short_description = 'Artist'  # Set the column name for 'artist' in admin list display
