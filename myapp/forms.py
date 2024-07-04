from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))

class UserRegisterForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class PhotoUploadForm(forms.Form):
    image = forms.ImageField()


COUNTRY_CHOICES = [
    ('USA', 'United States'),
    ('CA', 'Canada'),
    ('GB', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
]

CITY_CHOICES = [
    ('NY', 'New York'),
    ('LA', 'Los Angeles'),
    ('TOR', 'Toronto'),
    ('LDN', 'London'),
    ('PAR', 'Paris'),
]

class GameCreationForm(forms.Form):
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    num_players = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '6-20', 'class': 'form-control'}))
    game_amount = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Min. 10$', 'class': 'form-control'}))