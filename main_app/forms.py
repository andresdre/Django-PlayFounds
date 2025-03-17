from django import forms
from .models import Place, Review, Category

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'address', 'category', 'description', 'image']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter the address of the place'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe this place'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['place', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Leave a comment about this place'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe this category'}),
        }
