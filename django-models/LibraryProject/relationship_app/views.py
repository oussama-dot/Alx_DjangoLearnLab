from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ exact match
    context_object_name = "library"