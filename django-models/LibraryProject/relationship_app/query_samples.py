from . import models
from models import Author,Book,Library,Librarian
library_name = "Central Library"

# 1. Get the library object by name
library = Library.objects.get(name=library_name)

# 2. Get all books in that library
books = library.books.all()

