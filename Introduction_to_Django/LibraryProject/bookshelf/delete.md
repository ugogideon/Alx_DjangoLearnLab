DELETE
### Delete Operation

**Objective**: Delete the book with the title "Nineteen Eighty-Four" and confirm the deletion by retrieving all books.

**Python Command**:

```python
from bookshelf.models import Book

# Retrieve the Book instance by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()  # Expected output: <QuerySet []>
