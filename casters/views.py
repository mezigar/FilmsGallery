from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Caster

class CasterListView(ListView):
    model = Caster
    template_name = 'caster_list.html'


class CasterDetailView(DetailView):
    model = Caster
    template_name = 'caster_detail.html'


class CasterCreateView(CreateView):
    model = Caster
    template_name = 'caster_new.html'
    fields = "__all__"
    success_url = reverse_lazy('caster_detail')

class CasterUpdateView(UpdateView):
    model = Caster
    template_name = 'caster_edit.html'
    fields = "__all__"


class CasterDeleteView(DeleteView):
    model = Caster
    template_name = 'caster_delete.html'
    success_url = reverse_lazy('caster_list')