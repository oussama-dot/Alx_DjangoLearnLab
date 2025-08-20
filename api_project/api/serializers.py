# api/serializers.py

from rest_framework import serializers
from .models import Book  # ✅ Import Book from models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
