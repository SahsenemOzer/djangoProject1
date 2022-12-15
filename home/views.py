from django.shortcuts import render
from unicodedata import category


# Create your views here.

def index(request):
    text="Merhaba Dünya"
    context={'text':text,
             'category': category}
    return render(request, 'index.html', context)
