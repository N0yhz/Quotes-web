from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Username'
                                   }))
    email = forms.CharField(max_length=100,
                            required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Email'
                                 }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Password'
                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Repeat Password'
                                    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fierlds = ['username', 'password']

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ['avatar']