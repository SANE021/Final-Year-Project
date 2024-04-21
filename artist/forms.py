from django import forms
from .models import Artist
from songs.models import Song

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'profile_pic', 'tagline', 'bio', 'gender', 'Nationality', 'Address']

    def __init__(self, *args, **kwargs):
        super(ArtistForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs['class'] = 'form-control'  # Add any additional widget attributes as needed


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['artist']  # Exclude the 'artist' field from the form fields
        fields = ['songThumbnail', 'song', 'songName', 'genre']  # Optionally, include other fields

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SongForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['artist'].initial = user.pk  # Set the initial value of 'artist' to the user's pk
            self.fields['artist'].widget = forms.HiddenInput()  # Hide the 'artist' field from the form