from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookListViewTest(APITestCase):
    def setUp(self):
        # Create an author and a book to test with
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')  # Uses the name from your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_create_book_authenticated(self):
        # Create user and log in
        user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, "New Book")
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Blocked Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
        def test_update_book_authenticated(self):
         user = User.objects.create_user(username="updater", password="testpass")
        self.client.login(username="updater", password="testpass")

        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            "title": "Updated Book Title",
            "publication_year": 2025,
            "author": self.author.id
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")
