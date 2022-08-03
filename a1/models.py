from django.db import models

# Create your models here.
class Vocab(models.Model):
    vocab_name = models.CharField(max_length=20)
    ans = models.CharField(max_length=20)
    def __str__(self):
        return self.vocab_name
