from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, TAInfo

class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

class TASignUpForm(UserCreationForm):
    class_tutoring = forms.CharField(max_length=100)
    times_available = forms.CharField(max_length=100)
    days_available = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']