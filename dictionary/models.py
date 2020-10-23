from django.db import models

# Create your models here.


class DictionaryEntry(models.Model):
    vo = models.TextField()
    fr = models.TextField()

    class Meta:
        db_table = 'defs'
