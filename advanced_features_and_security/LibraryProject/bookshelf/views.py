from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return HttpResponse("Book created (only for users with can_create)")

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Editing {book.title} (only for users with can_edit)")

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    return HttpResponse(f"Deleted {pk} (only for users with can_delete)")
