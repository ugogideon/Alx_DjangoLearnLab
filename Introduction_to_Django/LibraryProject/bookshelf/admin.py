from django.contrib import admin
from .models import Book  # Import the Book model

# Register the Book model with the admin site
admin.site.register(Book)
