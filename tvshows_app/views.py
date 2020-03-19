from django.shortcuts import render
from .models import *

def index(request):
    context = {
        "shows":Show.objects.all()
    }
    return render(request, 'index.html', context)
