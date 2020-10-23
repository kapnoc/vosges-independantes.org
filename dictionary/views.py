from django.shortcuts import render
from django.http import HttpResponse
from .models import DictionaryEntry

# Create your views here.


def index(request):
    fr_filter = request.GET.get('fr', None)
    vo_filter = request.GET.get('vo', None)
    entries = []
    if fr_filter or vo_filter:
        entries = DictionaryEntry.objects.using('base_dictionary')
    if fr_filter:
        entries = entries.filter(fr__icontains=fr_filter)
    if vo_filter:
        entries = entries.filter(vo__icontains=vo_filter)
    context = {
        'fr': fr_filter,
        'vo': vo_filter,
        'entries': entries,
    }
    return render(request, 'dico/index.html', context)
