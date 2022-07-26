from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookBaseView(View):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_all')


class BookListView(BookBaseView, ListView):
    """View to list all books.
    Use the 'book_list' variable in the template
    to access all Book objects"""

    template_name = "book_list.html"


class BookCreateView(BookBaseView, CreateView):
    """View to create a new book"""

    template_name = "book_form.html"


class BookUpdateView(BookBaseView, UpdateView):
    """View to update an book"""

    template_name = "book_form.html"


class BookDeleteView(BookBaseView, DeleteView):
    """View to delete an book"""
