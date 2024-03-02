from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['firstname', 'lastname', 'email', 'service', 'date', 'number_of_hours', 'genre', 'phone_number']