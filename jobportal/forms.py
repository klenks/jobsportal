from django.contrib.auth.models import User
from django import forms

from .models import Job, Resume, Person

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class JobForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Job
        fields = ['name']


class ResumeForm(forms.ModelForm):
    resume_file = forms.FileField()

    class Meta:
        model = Resume
        fields = ['resume_file']
