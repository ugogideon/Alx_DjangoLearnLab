from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from relationship_app.models import Author  # Import the Author model
from bookshelf.models import Book  # Import the Book model

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)  # Optional field
    nationality = models.CharField(max_length=50, null=True, blank=True)  # Optional field

    def __str__(self):
        return self.name

# Book Model with Custom Permissions
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    publication_year = models.IntegerField()  # Publication year

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)  # Name of the library
    books = models.ManyToManyField(Book)  # ManyToMany relationship to Book

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Name of the librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # OneToOne relationship to Library

    def __str__(self):
        return self.name

# UserProfile Model for Role-based User Permissions
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Updated to use CustomUser
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

# Signal to create a UserProfile when a new user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
