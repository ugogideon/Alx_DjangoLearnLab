# query_samples.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with the actual name of your project
django.setup()

from bookshelf.models import Book
from relationship_app.models import Library, Librarian
from relationship_app.models import Author  # Ensure you import the Author model

def query_all_books_by_author(author_name):
    # Query all books by a specific author
    try:
        author = Author.objects.get(name=author_name)  # Get the author instance
        books = Book.objects.filter(author=author)  # Filter books by the author instance
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

def list_all_books_in_library(library_name):
    # List all books in a library
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Get all books related to the library
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

def retrieve_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'.")

if __name__ == "__main__":
    # Example queries
    query_all_books_by_author("George Orwell")  # Replace with an actual author name
    list_all_books_in_library("Central Library")  # Replace with an actual library name
    retrieve_librarian_for_library("Central Library")  # Replace with an actual library name
