# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('add/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing a specific book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # URL for deleting a specific book
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view for Library
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # Logout view
    path('register/', views.register, name='register'),  # User registration view
    path('admin/', views.admin_view, name='admin_view'),  # Admin-specific view
    path('librarian/', views.librarian_view, name='librarian_view'),  # Librarian-specific view
    path('member/', views.member_view, name='member_view'),  # Member-specific view
]
