# Views.py
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsBookOwner

# Creating my BookList view here.
class BookList(generics.ListAPIView):
    """
    A view for listing all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on the Book model.
    Authentication is required to access any endpoint in this ViewSet.
    Permissions are set based on user roles.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

# Defining permission classes
permission_classes = [IsAuthenticated]  # Only authenticated users can access

# For admin access, you can use IsAdminUser
    # permission_classes = [IsAdminUser]  # Only admins can access
