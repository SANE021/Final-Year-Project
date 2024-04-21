from django.shortcuts import render, redirect
import requests
from .forms import BookingForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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


def khalti_payment(request):
    return render(request, 'services/khalti_payment.html')


@csrf_exempt
def verify_payment(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "test_secret_key_4163c7a8aa78468680a3b540d68ccb12"
   }
   

   response =   requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}",safe=False)