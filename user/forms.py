from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class JoinForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email','name']


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']