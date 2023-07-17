from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import JoinForm, LoginForm, ProfileForm
from django.contrib.auth import get_user_model
from .models import Profile as Profiles

User = get_user_model()

class Join(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = JoinForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_join.html', context)
    
    def post(self, request):
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')

        form.add_error(None, '회원가입 양식을 지켜주세요.')
        context = {
            'form': form
        }
        return render(request, 'user/user_join.html', context)
### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)
    
    
### Logout
class Logout(View):
    def get(self, request):
            logout(request)
            return redirect('blog:list')
        
### Profile
class Profile(View):
    def get(self, request):

        if request.user.is_profile:
            return redirect('user:pf-edit')
        
        form = ProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_profile.html', context)
        
    def post(self, request):
        
        user = User.objects.get(pk=request.user)
        avatarUrl = request.FILES['avatarUrl']
        name = request.POST['name']
        
        profile = Profiles.objects.create(user=user, avatarUrl=avatarUrl, name=name)
        user.is_profile = True
        user.save()
        
        return redirect('blog:list')
    

class ProfileUpdate(View):
    def get(self, request):
        profile = Profiles.objects.get(user=request.user)
        form = ProfileForm(initial={'avatarUrl': profile.avatarUrl, 'name': profile.name})
        context = {
            'form': form,
        }
        return render(request, 'user/user_pf_edit.html', context)
        
    def post(self, request):
        
        user = User.objects.get(pk=request.user)
        avatarUrl = request.FILES['avatarUrl']
        name = request.POST['name']
        
        profile = Profiles.objects.get(user=user)
        profile.avatarUrl = avatarUrl
        profile.name = name
        profile.save()
        
        return redirect('blog:list')