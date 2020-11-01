from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'"{self.name}" (tag)'


class MarkdownPage(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    body = MartorField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'"{self.title}" (page)'

    class Meta:
        abstract = True


class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    contents = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'"{self.name}" (image)'
