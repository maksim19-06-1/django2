from django import forms
from django.forms import ModelForm
from .models import Flight, Airport

class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields = ['origin','destination','duration']
        # fields = '__all__'

class AirportForm(ModelForm):
    class Meta:
        model=Airport
        fields = '__all__'