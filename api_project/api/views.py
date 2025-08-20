# api/views.py

from rest_framework import generics, viewsets
from .models import Book  # ✅ Import the model from models.py
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
