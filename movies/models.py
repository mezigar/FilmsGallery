from audioop import reverse
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    # director = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])
    

class Caster(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    role = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.first_name + self.last_name

