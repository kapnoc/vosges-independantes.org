from django.db import models

from martor.models import MartorField
from utils.models import MarkdownPage


class NaturePage(MarkdownPage):

    class Meta:
        app_label = 'nature'
