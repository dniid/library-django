from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


class AuthorBaseView(View):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author_all')


class AuthorListView(AuthorBaseView, ListView):
    """View to list all authors.
    Use the 'author_list' variable in the template
    to access all Author objects"""

    template_name = "author_list.html"


class AuthorCreateView(AuthorBaseView, CreateView):
    """View to create a new author"""

    template_name = "author_form.html"


class AuthorUpdateView(AuthorBaseView, UpdateView):
    """View to update an author"""

    template_name = "author_form.html"


class AuthorDeleteView(AuthorBaseView, DeleteView):
    """View to delete an author"""
