from django import forms
from userapp.models import Logins


class UserForm(forms.ModelForm):
    class Meta:
        model = Logins
        fields = ['username','password','usertype']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'password': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'confirm_password': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}),
            'usertype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Type'})
        }


class UserFormcreate(forms.ModelForm):
    class Meta:
        model = Logins
        fields = ['username','password','confirm_password','usertype']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'password': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'confirm_password': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}),
            'usertype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Type'})
        }


