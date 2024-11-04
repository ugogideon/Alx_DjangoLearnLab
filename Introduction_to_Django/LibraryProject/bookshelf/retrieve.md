GET
### Retrieve Operation

**Objective**: Retrieve and display all attributes of the book created with the title "1984", author "George Orwell", and publication year 1949.

**Python Command**:

```python
from bookshelf.models import Book

# Retrieve the Book instance by title
book = Book.objects.get(title="1984")

# Display all attributes of the retrieved book
book.title, book.author, book.publication_year  # Expected output: ('1984', 'George Orwell', 1949)
