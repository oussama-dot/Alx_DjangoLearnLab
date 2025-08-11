from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: Get all books by a specific author ---
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# --- Query 2: Get all books in a specific library ---
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

# --- Query 3: Retrieve the librarian for a library ---
librarian = Librarian.objects.get(library=library)
print(librarian.name)
