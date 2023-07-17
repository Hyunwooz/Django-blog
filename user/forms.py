from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

User = get_user_model()

class JoinForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email']


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatarUrl', 'name']