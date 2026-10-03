from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Person

# LIST
class PersonListView(ListView):
    model = Person
    template_name = 'myapp/person_list.html'
    context_object_name = 'persons'

# DETAIL
class PersonDetailView(DetailView):
    model = Person
    template_name = 'myapp/person_detail.html'
    context_object_name = 'person'

# CREATE
class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name', 'last_name']
    template_name = 'myapp/person_create.html'
    success_url = reverse_lazy('person_list')

# UPDATE
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name', 'last_name']
    template_name = 'myapp/person_update.html'
    success_url = reverse_lazy('person_list')

# DELETE
class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'myapp/person_delete.html'
    success_url = reverse_lazy('person_list')
