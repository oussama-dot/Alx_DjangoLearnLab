from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for Book model with custom validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation: Ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# BookSerializer serializes all fields of Book, including validation.
# AuthorSerializer includes a nested serialization of all books written by the author.
