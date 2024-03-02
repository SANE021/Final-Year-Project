from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('accounts.urls')),
    path('artist/',include('artist.urls')),
    path('song/', include('songs.urls')), 
    path('booking/', include('booking.urls')), 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
