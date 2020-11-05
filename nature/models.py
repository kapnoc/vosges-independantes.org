from django.db import models

from django_kapnoc.models import MarkdownPage


class NaturePage(MarkdownPage):
    class Meta:
        app_label = 'nature'
