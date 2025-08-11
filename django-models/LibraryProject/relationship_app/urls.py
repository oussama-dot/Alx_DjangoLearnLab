from django.urls import path
from .views import user_login, user_logout, register, list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # your existing view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # existing CBV

    # Auth URLs
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]
