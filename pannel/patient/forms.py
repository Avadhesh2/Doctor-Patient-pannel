# In forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=100, required=True, help_text='Required.')
    city = forms.CharField(max_length=100, required=True, help_text='Required.')
    state = forms.CharField(max_length=100, required=True, help_text='Required.')
    pincode = forms.CharField(max_length=6, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode',)

