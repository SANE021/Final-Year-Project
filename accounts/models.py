from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def get_artist(self):
        if(hasattr(self,'artist')):
            return self.artist
        return None