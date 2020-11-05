from django.db import models

from martor.models import MartorField
from django_kapnoc.models import MarkdownPage


class NaturePage(MarkdownPage):
    description = models.TextField()
    body_vo = MartorField()

    class Meta:
        app_label = 'nature'
