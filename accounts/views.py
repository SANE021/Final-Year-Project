from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from songs.models import Song

def index(request):
    return render(request, 'home/index.html')

@login_required
def handle_login(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        # Handle the case when the user is not authenticated
        # You can redirect them to the login page or any other appropriate page
        return redirect('login')  # Change 'login' to the actual login URL


@login_required
def Dashboard(request):
    songs = Song.objects.all()
    return render(request, 'dashboard/dashboard.html', {'songs': songs})


# def Service(request):
#     return render(request, 'services/services.html')