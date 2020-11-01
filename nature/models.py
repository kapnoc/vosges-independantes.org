from django.db import models

from kapnoc_pages.models import MarkdownPage


class NaturePage(MarkdownPage):
    class Meta:
        app_label = 'nature'
