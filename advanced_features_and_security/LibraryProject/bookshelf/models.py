from django.db import models
from relationship_app.models import Author  # Assuming Author is in relationship_app

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # ForeignKey to Author
    publication_year = models.PositiveIntegerField()  # Publication year
    isbn = models.CharField(max_length=13, unique=True)  # Optional: ISBN for the book

    def __str__(self):
        return self.title
