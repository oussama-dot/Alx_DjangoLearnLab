import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()

from relationship_app.models import Book, Library

Book.objects.filter(author__name="John Doe")
