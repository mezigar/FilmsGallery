from django.db import models
from django.urls import reverse
from movies.models import Movie

class Caster(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    role = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie, related_name='films')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse('caster_detail', args=[str(self.id)])
