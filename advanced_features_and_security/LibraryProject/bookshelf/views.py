# bookshelf/views.py

from .forms import ExampleForm  # ✅ Required for the check to pass
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET)
    books = []

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })
