from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import * 
from django.views.generic import  DetailView



def songs_list(request):
    songs = Song.objects.all()  # Fetch all song objects from the database

    context = {
        'songs': songs,  # Pass the list of songs to the template
    }
    return render(request, 'Dashboard/Dashboard.html', context)

class SongDetailView(DetailView):
    model = Song
    template_name = 'dashboard/song_detail.html'


