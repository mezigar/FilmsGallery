from django.urls import path
from .views import CasterDetailView, CasterListView , CasterDeleteView, CasterCreateView, CasterUpdateView

urlpatterns = [
    path('', CasterListView.as_view(), name='caster_list'),
    path('<int:pk>/', CasterDetailView.as_view(), name='caster_detail'),
    path('<int:pk>/delete/', CasterDeleteView.as_view(), name='caster_delete'),
    path('<int:pk>/edit/', CasterUpdateView.as_view(), name='caster_edit'),
    path('new/', CasterCreateView.as_view(), name='caster_new'),
]
