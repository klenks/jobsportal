from django.contrib.auth.models import User
from django import forms

from .models import Job

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class JobForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Job
        fields = ['name']
