from django.db import models
from relationship_app.models import Author  # Import the Author model

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)  # Optional field
    nationality = models.CharField(max_length=50, null=True, blank=True)  # Optional field

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    publication_year = models.IntegerField()  # Publication year

 def __str__(self):
        return self.name
