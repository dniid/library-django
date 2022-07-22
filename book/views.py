from django.shortcuts import render, redirect
from book.forms import BookForm
from book.models import Book


def book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BookForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    books = Book.objects.all()
    return render(request, "show.html", {'books': books})


def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'edit.html', {'book': book})


def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'book': book})


def destroy(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/show")