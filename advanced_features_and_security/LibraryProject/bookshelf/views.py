from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .forms import ExampleForm

# View for searching books
def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View for creating a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Process form data to create book
        # Add form handling logic here
        pass
    return render(request, 'bookshelf/book_form.html')

# View for editing a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Process form data to update book
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

# View for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# View for viewing books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
