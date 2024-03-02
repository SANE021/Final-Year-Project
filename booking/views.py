from django.shortcuts import render, redirect
from .forms import BookingForm

# @login_required
def Service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            booking = form.save(commit=False)
            booking.owner = request.user  # Assuming you are using Django authentication
            booking.save()
            return redirect('success_page')  # Redirect to a success page or any other desired page
    else:
        form = BookingForm()

    return render(request, 'services/services.html', {'form': form})


def Booked(request):
    
    return render(request, 'booking/booked.html')