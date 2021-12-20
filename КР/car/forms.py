from django import forms
from django.forms import ModelForm
from .models import Manufacturer, Model

class ManufacturerForm(ModelForm):
    class Meta:
        model=Manufacturer
        fields = ['name','yearFoundation','chairman']
        # fields = '__all__'

class ModelForm(ModelForm):
    class Meta:
        model=Model
        fields = '__all__'
