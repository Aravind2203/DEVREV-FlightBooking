from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager
from django.utils import timezone 
# Create your models here.

class User(AbstractUser):
    username=None
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=UserManager()

class AirLine(models.Model):
    license_number=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='airline',null=True,blank=True)

    def __str__(self) :
        return self.name

class Airports(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    name=models.CharField(max_length=10)
    airline=models.ForeignKey(AirLine,on_delete=models.CASCADE)
    source=models.ForeignKey(Airports,on_delete=models.SET_NULL,blank=True,null=True,related_name="depart")
    destination=models.ForeignKey(Airports,on_delete=models.SET_NULL,blank=True,null=True,related_name="arrive")
    time_of_departure=models.TimeField(default=timezone.now().time())
    duration_of_travel=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Travel(models.Model):
    flight_id=models.ForeignKey(Flight,on_delete=models.CASCADE)
    remain=models.PositiveIntegerField(default=60)
    date=models.DateField(default=timezone.now().date())
    status=models.CharField(max_length=10)

    def __str__(self):
        return str(self.flight_id)+str(self.date)
    
class Passengers(models.Model):
    name=models.CharField(max_length=10)
    age=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Bookings(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    travel=models.ForeignKey(Travel,on_delete=models.SET_NULL,blank=True,null=True)
    passengers_count=models.PositiveIntegerField(default=1)
    passengers_names=models.ManyToManyField(Passengers)

    def __str__(self):
        return str(self.user_id)+str(self.id)

