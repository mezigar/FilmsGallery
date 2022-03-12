from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('film/<int:pk>/delete/', MovieDeleteView.as_view(), name="movie_delete"),
    path('film//<int:pk>/edit/', MovieUpdateView.as_view(), name ='movie_edit'),
    path('film/new/', MovieCreateView.as_view(), name = "movie_new"),
    path('', MovieListView.as_view(), name='home'),
    path('film/<int:pk>/', MovieDetailView.as_view(), name='movie_detail')
]
