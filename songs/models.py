from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Song(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each song is associated with an artist
    songThumbnail = models.ImageField(_("Song Thumbnail"), upload_to='thumbnail/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    song = models.FileField(_("Song"), upload_to='songs/', help_text=".mp3 supported only")
    songName = models.CharField(_("Song Name"), max_length=50)
    
    GENRE_TYPE = [
        ('C', 'Classical'),
        ('HH', 'Hip-Hop'),
        ('J', 'Jazz'),
        ('F', 'Funk'),
        ('R', 'R-N-B'),
        ('P', 'Pop'),
        ('RK', 'Rock'),
        ('M', 'Metal'),
    ]
    genre = models.CharField(max_length=2, choices=GENRE_TYPE, blank=False)
    
    created = models.DateTimeField(_("Song created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest song update"), auto_now=True)
    paginate_by = 2

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return self.songName
