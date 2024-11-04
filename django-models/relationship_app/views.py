# relationship_app/views.py

from django.shortcuts import render
from django.views import DetailView
from .models import Library  # Import both Book and Library models

def list_books(request):
    books = Book.objects.all()  # Retrieve all book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Path to the library detail template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add all books associated with the library to the context
        return context
