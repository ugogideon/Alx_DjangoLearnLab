PUT
### Update Operation

**Objective**: Update the title of the book from "1984" to "Nineteen Eighty-Four" and save the changes.

**Python Command**:

```python
from bookshelf.models import Book

# Retrieve the Book instance by title
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated title
book.title  # Expected output: 'Nineteen Eighty-Four'
