from django import forms
from relationship_app.models import Book, Author
from .models import Book
# Book Form for Creating and Editing Books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'publication_year': 'Year of Publication',
        }

class ExampleForm(forms.Form):
    # Example form fields
    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}))
    author = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}))
    publication_year = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}))
       
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit the queryset for authors to all available Author objects
        self.fields['author'].queryset = Author.objects.all()

# Book Search Form (used for search functionality)
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
