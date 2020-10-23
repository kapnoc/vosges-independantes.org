from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Accueil'
    }
    return render(request, 'home/index.html', context)
