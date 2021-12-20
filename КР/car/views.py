from django.shortcuts import render
from django.http import HttpResponse
from .forms import ManufacturerForm,ModelForm
from rest_framework.decorators import action
from .models import Manufacturer, Model
def index():
    pass

def index(request):
    form = ManufacturerForm(request.POST)
    if form.is_valid():
        form.save()
    form = ManufacturerForm()
    
    form2 = ModelForm(request.POST)
    if form2.is_valid():
        form2.save()
    form2 = ModelForm()

    return render(request,"car/index.html", {"model": Model.objects.all(),'form':form,'form2':form2})

def ex1(request, id=0):
    if(id!=0):
        return render(request, "car/ex1.html", {"id": int(id),"exams": Model.objects.all(),"sessionUniversity": Manufacturer.objects.all()})
        
    return render(request,"car/ex1.html", {"sessionUniversity": Manufacturer.objects.all()})

def ex2(request):
    
    return render(request,"car/ex2.html")
