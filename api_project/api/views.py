from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Creating my Booklist views here.

class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
