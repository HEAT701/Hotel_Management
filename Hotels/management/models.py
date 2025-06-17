from django.db import models
# Create your models here.

class Room(models.Model):
    ROOM_TYPE ={
        ("SINGLE","SINGLE"),
        ("DUBLE","DUBLE"),
        ("FAMILY","FAMILY")
    }
    Number = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=ROOM_TYPE)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)

    
    def __str__(self):
        return f"Room {self.Number} - {self.type}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - Room {self.room.Number}"
    
class Hotel(models.Model):
    Name = models.CharField(max_length=50)
    Locations = models.CharField(max_length=60)
    Room = models.ForeignKey(Room,on_delete=models.CASCADE)
    Booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
