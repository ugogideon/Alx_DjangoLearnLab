# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Initialize the router
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    
    # Other URLs...
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
