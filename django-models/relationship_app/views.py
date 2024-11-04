# relationship_app/views.py

from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Retrieve all book instances from the database
    return render(request, 'list_books.html', {'books': books})  # Render the list_books.html template with the context

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template to use

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add all books associated with the library to the context
        return context
        