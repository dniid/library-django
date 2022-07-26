from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Catalog


class CatalogBaseView(View):
    model = Catalog
    fields = '__all__'
    success_url = reverse_lazy('catalog_all')


class CatalogListView(CatalogBaseView, ListView):
    """View to list all catalogs.
    Use the 'catalog_list' variable in the template
    to access all Catalog objects"""

    template_name = "catalog_list.html"


class CatalogCreateView(CatalogBaseView, CreateView):
    """View to create a new catalog"""

    template_name = "catalog_form.html"


class CatalogUpdateView(CatalogBaseView, UpdateView):
    """View to update an catalog"""

    template_name = "catalog_form.html"


class CatalogDeleteView(CatalogBaseView, DeleteView):
    """View to delete an catalog"""
