from django.shortcuts import render, redirect
from book.forms import BookForm
from book.models import Book


def create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('bread')
            except:
                pass
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


def read(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {'books': books})


def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect("bread")
    return render(request, 'book_form.html', {'form': form})


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("bread")
