from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import JoinForm, LoginForm, ProfileForm
from .models import Profile as ProfileModel

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
            user = form.save()
            profile = ProfileModel.objects.create(user=user)
            return redirect('user:login')

        form.add_error(None,'양식을 확인해주세요.')
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
            
        form.add_error(None, '양식을 확인해주세요.')
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')


class ChangePassWord(View):
    def get(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        context = {
            'form': form
        }
        return render(request,'user/user_change_pw.html',context)
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('blog:list')
        
        form.add_error(None,'Error 발생')
        context = {
            'form': form
        }
        return render(request,'user/user_change_pw.html',context)


class ProfileUpdate(LoginRequiredMixin,View):
    Mixin : LoginRequiredMixin
    login_url = '/user/login'
    redirect_field_name = 'next'
    
    def get(self, request):
        profile = ProfileModel.objects.get(user=request.user.pk)
        form = ProfileForm(initial={'avatarUrl': profile.avatarUrl, 'name': profile.name , 'aboutMe': profile.aboutMe})
        context = {
            'form': form,
            'type': 'edit'
        }
        return render(request, 'user/user_profile.html', context)
        
    def post(self, request):
        
        user = User.objects.get(pk=request.user.pk)
        profile = ProfileModel.objects.get(user=user)
        name = request.POST['name']
        aboutMe = request.POST['aboutMe']
        
        try:
            avatarUrl = request.FILES['avatarUrl']
        except:
            profile.name = name
            profile.aboutMe = aboutMe
        else:
            profile.name = name
            profile.avatarUrl = avatarUrl
            profile.aboutMe = aboutMe
        
        profile.save()
        return redirect('blog:list')
