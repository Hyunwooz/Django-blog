from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Join, Login, Logout, Profile, ProfileUpdate

app_name = 'user'

urlpatterns = [
    path("join/", Join.as_view(), name='join'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name='logout'),
    path("profile/create/", Profile.as_view(), name='profile'),
    path("profile/edit/", ProfileUpdate.as_view(), name='pf-edit'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)