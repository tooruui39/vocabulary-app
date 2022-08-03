from django.db import models

# Create your models here.
class Read(models.Model):
    titles = models.CharField(max_length=9999, null=True, blank=True)
    words = models.CharField(max_length=99999, null=True, blank=True)
    def __str__(self):
        return self.titles
