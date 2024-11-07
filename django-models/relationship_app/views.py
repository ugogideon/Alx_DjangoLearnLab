# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # Importing DetailView for class-based view
from .models import Library  # Importing the Book and Library models
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def list_books(request):
    books = Book.objects.all()  # Retrieve all book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Path to the library detail template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add all books associated with the library to the context
        return context

# Custom Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('home')  # Redirect to a home page or another view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Liberian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (restricted to Admins)
@userpassestest(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view (restricted to Librarians)
@userpassestest(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view (restricted to Members)
@user_
Checks for “Utilize the @userpassestest decorator to check the user’s role before granting access to each view.” task

relationship_app/views.py doesn't contain: ["relationship_app/member_view.html", "relationship_app/librarian_view.html", "relationship_app/admin_view.html"]passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
