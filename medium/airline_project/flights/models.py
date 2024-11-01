from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.flight_number} to {self.destination}"

class Passenger(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for {self.passenger.name}"
