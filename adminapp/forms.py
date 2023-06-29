from django.forms import ModelForm
from django import forms
from user.models import AirLine,Airports,Flight,Travel
from django.contrib.admin.widgets import AdminDateWidget
class AirLineForm(ModelForm):
    class Meta:
        model=AirLine
        fields=['license_number','name']
    
class AirPortForm(ModelForm):
    class Meta:
        model=Airports
        fields=['name']

class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields=['name','airline','source','destination','duration_of_travel']

class TravelForm(ModelForm):
    
    class Meta:
        model=Travel
        fields=['flight_id']
        
