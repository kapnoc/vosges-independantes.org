from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Tag(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'"{self.name}" (tag)'


class MarkdownPage(models.Model):
    title = models.TextField()
    tags = models.ManyToManyField(Tag)
    body = MartorField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
