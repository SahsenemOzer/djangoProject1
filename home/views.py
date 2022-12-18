from django.shortcuts import render
#from unicodedata import category



# Create your views here.

def index(request):
    text = "Merhaba Dunya"
    context = {'text': text}

    return render(request, 'index.html', context)
