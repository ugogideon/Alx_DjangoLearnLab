from django.contrib import admin
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the admin interface
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality
    search_fields = ('title', 'author')
    
# Register the Book model with the admin site
admin.site.register(Book)
