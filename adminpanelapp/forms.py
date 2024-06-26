from django import forms
from .models import Book,Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author Name'})
        }
        # widgets:{
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author Name'}),
        # }




class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Quantity'}),

            # 'image':forms.ImageField(attrs={'class':'form-control-file','placholder':'select image'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Book Author'})
        }
