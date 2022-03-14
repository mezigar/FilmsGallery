from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from movies.models import Movie


class Post(models.Model):
    author = models.ForeignKey(
        'accounts.CustomUser', 
        on_delete=models.CASCADE,
        )
    body = models.TextField()
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    