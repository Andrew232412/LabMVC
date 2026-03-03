from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import BookForm
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_list.html"


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("books:list")
    return render(request, "books/book_form.html", {"form": form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("books:list")
    return render(request, "books/book_form.html", {"form": form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("books:list")
    return render(request, "books/book_confirm_delete.html", {"book": book})
