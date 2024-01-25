from django.db import models

from django.urls import reverse

# FINCH MODEL
class Finch(models.Model):
    name = models.CharField(max_length=25)
    breed = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})