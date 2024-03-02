from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Booking(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    
    email = models.CharField(max_length=30)
    SERVICE_TYPE = [
        ('VR', 'Vocal-Recording'),
        ('MM', 'Mix-Master'),
        ('FSB', 'Full-Song-Beat'),
        ('FSOB', 'Full-Song-Own-Beat'),
        ('AMCD','Album-music-cover-design'),
        ('BP', 'Beat-Production'),
        ('MVE','Music-Video-Recording'),
    ]
    service = models.CharField(max_length=4, choices=SERVICE_TYPE, blank=False)
    date = models.DateField(max_length=10,blank=False)
    number_of_hours = models.IntegerField(blank=False)
    GENRE_TYPE = [
        ('C', 'Classical'),
        ('HH', 'Hip-Hop'),
        ('J', 'Jazz'),
        ('F', 'Funck'),
        ('R','R-N-B'),
        ('P', 'Pop'),
        ('RK','Rock'),
        ('M','Metal'),
    ]
    genre = models.CharField(max_length=2, choices=GENRE_TYPE, blank=False)
    phone_number =models.CharField(max_length=10,blank=False)

    

    def __str__(self):
        return f"{self.id} | {self.owner} | {self.service} | {self.genre}"
