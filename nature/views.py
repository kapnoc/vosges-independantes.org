from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from django_kapnoc.models import Tag
from .models import NaturePage


def index(request):
    tags = Tag.objects.all()[:]
    pages = NaturePage.objects.all()[:]
    context = {
        'title': 'Nature',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'nature/index.html', context)


def tag_pk(request, pk):
    try:
        queried_tag = Tag.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.all()[:]
    pages = NaturePage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'Nature - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'nature/index.html', context)


def tag_name(request, name):
    try:
        queried_tag = Tag.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.all()[:]
    pages = NaturePage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'Nature - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'nature/index.html', context)


def page(request, pk):
    try:
        page = NaturePage.objects.get(pk=int(pk))
    except ObjectDoesNotExist:
        raise Http404("Page does not exist")
    context = {
        'title': f'Nature - {page.title}',
        'page': page,
    }
    return render(request, 'nature/page.html', context)
