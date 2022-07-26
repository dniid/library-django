from django import forms
from catalog.models import Catalog


class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = "__all__"
