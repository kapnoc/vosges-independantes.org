from django.shortcuts import render
from django.http import HttpResponse
from .models import DictionaryEntry

# Create your views here.


def dictionary(request):
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
    return render(request, 'loguedje/dictionary.html', context)


def translate(request):
    fr_query = request.GET.get('fr', None)
    vo_query = request.GET.get('vo', None)
    fr_result = None
    vo_result = None
    entries = []
    if fr_query or vo_query:
        entries = DictionaryEntry.objects.using('base_dictionary')
    if fr_query:
        cleaned_query = fr_query.replace(',', ' ')
        split_query = cleaned_query.split()
        results = []
        for fr_word in split_query:
            try:
                vo_word = entries.filter(fr=fr_word)[0]
                results.append(vo_word.vo)
            except:
                results.append(fr_word)
        vo_result = ' '.join(results)
    if vo_query:
        pass
    context = {
        'fr': fr_query if fr_query else fr_result,
        'vo': vo_query if vo_query else vo_result,
    }
    return render(request, 'loguedje/translate.html', context)
