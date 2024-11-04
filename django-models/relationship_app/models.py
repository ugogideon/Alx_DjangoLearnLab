from django.db import models
from relationship_app.models import Author  # Import the Author model
from bookshelf.models import Book  # Import the Book model
from .models import Library  # Import the Library model

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)  # Optional field
    nationality = models.CharField(max_length=50, null=True, blank=True)  # Optional field

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    publication_year = models.IntegerField()  # Publication year

class Library(models.Model):
    name = models.CharField(max_length=100)  # Name of the library
    books = models.ManyToManyField(Book)  # ManyToMany relationship to Book

class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Name of the librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # OneToOne relationship to Library
    
 def __str__(self):
        return self.name
