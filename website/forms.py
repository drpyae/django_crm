from django.contrib.auth.forms import UserCreationFrom
from django.contrib.auth.models import User
from django import forms

class SignUpFrom(UserCreationFrom):
    email = forms.EmailField(label="", widget=froms.TextInput(attrs={'class':'from-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length="100", widget=froms.TextInput(attrs={'class':'from-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length="100", widget=froms.TextInput(attrs={'class':'from-control', 'placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')