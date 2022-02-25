from django.shortcuts import render

# Create your views here.
def get_booking_system(request):
    return render(request, 'booking.html')
