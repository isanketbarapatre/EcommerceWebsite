from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    pass1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs ={'class': 'form-control'}))
    pass2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs ={'class': 'form-control'}))
    email = forms.EmailField(required = True , label="Email", widget=forms.EmailInput(attrs ={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'pass1', 'pass2']

        widgets = {'username': forms.TextInput(attrs ={'class': 'form-control'})}


