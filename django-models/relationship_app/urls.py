# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
