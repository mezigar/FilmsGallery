from django.urls import path
# from posts.views import 

from .views import SignUpView
from posts.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('posts/<int:pk>/', PostListView.as_view(), name="home"),
#     path('posts/<int:pk>/new/', PostCreateView.as_view(), name='post_new'),
#     path('posts/<int:pk>/<int:id>/', PostDetailView.as_view(), name="post_detail"),
#     path('posts/<int:pk>/<int:id>/delete/', PostDeleteView.as_view(), name="post_delete"),
#     path('posts/<int:pk>/<int:id>/edit/', PostUpdateView.as_view(), name="post_edit"),


# ]

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('posts/', PostListView.as_view(), name="home"),
    path('posts/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),


]
