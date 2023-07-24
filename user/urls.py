from django.urls import path
from .views import Join, Login, Logout, ProfileUpdate, ChangePassWord

app_name = 'user'

urlpatterns = [
    path("join/", Join.as_view(), name='join'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name='logout'),
    path("changePassword/", ChangePassWord.as_view(), name='change-pw'),
    path("profile/edit/", ProfileUpdate.as_view(), name='pf-edit'),
] 

