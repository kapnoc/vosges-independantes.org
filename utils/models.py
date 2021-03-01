from django.db import models
from martor.models import MartorField


class Tag(models.Model):
    name_fr = models.CharField(max_length=255)
    name_vo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'"{self.name_fr} | {self.name_vo}" (tag {self.pk})'


class MarkdownPage(models.Model):
    title_fr = models.CharField(max_length=255)
    title_vo = models.CharField(max_length=255)
    description_fr = models.TextField()
    description_vo = models.TextField()
    tags = models.ManyToManyField(Tag)
    body_fr = MartorField()
    body_vo = MartorField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'"{self.title_fr} | {self.title_vo}" (page {self.pk})'

    class Meta:
        abstract = True
