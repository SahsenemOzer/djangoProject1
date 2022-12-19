from django.shortcuts import render
#from unicodedata import category



# Create your views here.

def index(request):
    text = "Merhaba Dunya"
    context = {'text': text}

    return render(request, 'index.html', context)
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
