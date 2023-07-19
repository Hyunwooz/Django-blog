from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

User = get_user_model()

class JoinForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatarUrl', 'name' , 'aboutMe']