from django.shortcuts import render
from .models import Flight, Passenger, Booking

def flights_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights_list.html', {'flights': flights})

def flight_detail(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flight_detail.html', {'flight': flight})