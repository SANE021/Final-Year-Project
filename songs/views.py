from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import * 
from django.utils.decorators import method_decorator
from django.views.generic import  DetailView ,ListView



def songs_list(request):
    songs = Song.objects.all()  # Fetch all song objects from the database

    context = {
        'songs': songs,  # Pass the list of songs to the template
    }
    return render(request, 'Dashboard/Dashboard.html', context)

class SongDetailView(DetailView):
    model = Song
    template_name = 'dashboard/song_detail.html'

@method_decorator(login_required, name='dispatch')
class MySongsView(ListView):
    model = Song
    template_name = 'artist/my_songs.html'
    context_object_name = 'user_songs'

    def get_queryset(self):
        # Filter songs based on the currently logged-in user
        return Song.objects.filter(artist=self.request.user.artist)

