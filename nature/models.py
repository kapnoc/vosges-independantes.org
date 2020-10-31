from django.db import models

from markdownpages.models import MarkdownPage


class NaturePage(MarkdownPage):
    class Meta:
        app_label = 'nature'
