from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movie_new.html'
    fields = "__all__"

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie_edit.html'
    fields =  ['title', 'description']


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('home')
