# myapp/forms.py
from django import forms
from .models import *

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'mobile_number', 'password', 'address']

class TaskForm(forms.ModelForm):
    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = ['name', 'date_time', 'assigned_to']