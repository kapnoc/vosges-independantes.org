from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from utils.models import Tag
from .models import NaturePage


class NaturePageListView(ListView):
    model = NaturePage
    template_name = 'nature/naturepage-list.html'

    def get_queryset(self):
        if self.kwargs.get('tag', "") != "":
            self.tag = get_object_or_404(Tag, name_vo=self.kwargs['tag'])
            return self.tag.naturepage_set.all()
        else:
            self.tag = None
            return NaturePage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.filter(
            naturepage__isnull=False,
        )[:]
        context['title'] = f"Nature"
        context['tags'] = tags
        return context


class NaturePageDetailView(DetailView):
    model = NaturePage
    template_name = 'nature/naturepage-detail.html'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title_fr} - {self.object.title_vo} - Nature"
        return context
