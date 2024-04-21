from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Artist
from django.contrib import messages
from .forms import ArtistForm ,SongForm
from songs.models import Song
from django.views import View



@login_required
def create_artist_profile(request):
    if (existing_artist := request.user.get_artist()):
        return redirect('dashboard')  # Redirect to dashboard if the artist profile already exists

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)

        if form.is_valid():
            artist = form.save(commit=False)
            artist.owner = request.user
            artist.save()
            return redirect('dashboard')
    else:
        form = ArtistForm()

    return render(request, 'dashboard/create_artist_profile.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ArtistProfileView(View):
    
    template_name = 'artist/profile.html'
    

    def get(self, request):
        artist = request.user.artist
        
        return render(request, self.template_name, {'artist': artist})



@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'artist/edit_profile.html'

    def get(self, request):
        artist = request.user.artist
        form = ArtistForm(instance=artist)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        artist = request.user.artist
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_profile')

        return render(request, self.template_name, {'form': form})
    
    

@login_required
def upload_song(request):
    genres = Song.objects.values_list('genre', flat=True).distinct()
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = request.user  # Set the artist to the current logged-in user
            song.save()
            messages.success(request, 'Song uploaded successfully.')
            return redirect('dashboard')  # Change this to the appropriate URL
    else:
        form = SongForm()

    return render(request, 'songs/upload_song.html', {'form': form, 'genres': genres})



    
    
@login_required
def edit_song(request, song_id):
    song = Song.objects.get(pk=song_id)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song updated successfully.')
            return redirect('dashboard')  # Change this to the appropriate URL
    else:
        form = SongForm(instance=song)

    return render(request, 'songs/edit_song.html', {'form': form, 'song': song})

 # Change this to the appropriate URL@login_required
def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)

    if request.method == 'POST':
        song.delete()
        messages.success(request, 'Song deleted successfully.')
        return redirect('dashboard')

    return render(request, 'songs/confirm_delete_song.html', {'song': song})