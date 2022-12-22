from django.shortcuts import render
from django.http.response import HttpResponse
from .models import house
from product.models import Category



# Create your views here.

def index(request):
    data = {
        "house" : house.objects.all()
    }

    return render(request, 'index.html',data)
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def properties(request):
    data = {
        "house" : house.objects.all()
    }
    return render(request, 'properties.html', data)

def propertySingle(request):
    return render(request, 'property-single.html')



