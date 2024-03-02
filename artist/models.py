from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Artist(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    tagline = models.CharField(max_length=100)
    bio =models.TextField(blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NS', 'Rather not to say'),
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    Nationality = models.TextField(blank=True)
    Address = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.id} | {self.name}"

