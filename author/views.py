from django.shortcuts import render, redirect
from author.forms import AuthorForm
from author.models import Author


def create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('aread')
            except:
                pass
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})


def read(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {'authors': authors})


def update(request, id):
    author = Author.objects.get(id=id)
    form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
        return redirect("aread")
    return render(request, 'author_form.html', {'form': form})


def delete(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect("aread")
