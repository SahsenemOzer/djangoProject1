from django.shortcuts import render
from django.http.response import HttpResponse
from .models import house, comment, mesaj
from product.models import Category


# Create your views here.

def index(request):
    data = {
        "house": house.objects.all()
    }

    return render(request, 'index.html', data)


def contact(request):
    if request.method == "POST":
        m = mesaj()
        m.name = request.POST["name"]
        m.email = request.POST["email"]
        m.baslik = request.POST["baslik"]
        m.mesaj = request.POST["mesaj"]
        m.save()

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    pid = {
        "comment": comment.objects.all()
    }
    return render(request, 'services.html', pid)


def properties(request):
    data = {
        "house": house.objects.all()
    }
    return render(request, 'properties.html', data)


def propertySingle(request):
    if request.method == "GET":
        getid = request.GET["id"]
        pid = {
            "id": getid,
            "house": house.objects.filter(id=getid),
            "comment": comment.objects.filter(houseid=getid)
        }

        return render(request, 'property-single.html', pid)

    if request.method == "POST":
        Y = comment()
        Y.name = request.POST["name"]
        Y.lastname = request.POST["lastname"]
        Y.email = request.POST["email"]
        Y.yorum = request.POST["yorum"]
        Y.houseid = request.POST["houseid"]
        Y.save()
        pid = {
            "id": request.POST["houseid"],
            "house": house.objects.filter(id=request.POST["houseid"]),
            "comment": comment.objects.filter(houseid=request.POST["houseid"]),
       }

        return render(request, 'property-single.html', pid)
    else:
        return render(request, 'property-single.html')

