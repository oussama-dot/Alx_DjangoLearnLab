from django.db import models
# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer