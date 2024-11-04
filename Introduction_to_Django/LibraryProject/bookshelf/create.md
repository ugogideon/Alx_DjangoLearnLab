POST
### Create Operation

**Objective**: Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.

**Python Command**:

```python
from bookshelf.models import Book

# Create a Book instance with the specified details
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output the created instance
book  # Expected output: <Book: 1984>
