from audioop import reverse
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    # director = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])
    


