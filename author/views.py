from django.shortcuts import render, redirect
from author.forms import AuthorForm
from author.models import Author


def aut(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = AuthorForm()
    return render(request, 'catalog_list.html', {'form': form})


def show(request):
    authors = Author.objects.all()
    return render(request, "show.html", {'authors': authors})


def edit(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'edit.html', {'author': author})


def update(request, id):
    author = Author.objects.get(id=id)
    form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'author': author})


def destroy(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect("/show")