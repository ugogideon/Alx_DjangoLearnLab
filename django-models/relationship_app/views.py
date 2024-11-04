# relationship_app/views.py

from django.shortcuts import render
from .models import Book

def list_books(request):
    # Query all books from the database
    books = Book.objects.all()  # Get all book instances
    return render(request, 'list_books.html', {'books': books})
