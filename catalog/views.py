from django.shortcuts import render, redirect
from catalog.forms import CatalogForm
from catalog.models import Catalog


def create(request):
    if request.method == "POST":
        form = CatalogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('read')
            except:
                pass
    else:
        form = CatalogForm()
    return render(request, 'catalog_form.html', {'form': form})


def read(request):
    catalogs = Catalog.objects.all()
    return render(request, "catalog_list.html", {'catalogs': catalogs})


def update(request, id):
    catalog = Catalog.objects.get(id=id)
    form = CatalogForm(request.POST, instance=catalog)
    if form.is_valid():
        form.save()
        return redirect("read")
    return render(request, 'catalog_form.html', {'form': form})


def delete(request, id):
    catalog = Catalog.objects.get(id=id)
    catalog.delete()
    return redirect("read")
