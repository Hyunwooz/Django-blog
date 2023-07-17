from django.urls import path
from .views import Index, Write, Detail, Delete, Update

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view() , name='list'),
    path('write/', Write.as_view() , name='write'),
    path('<int:pk>/', Detail.as_view() , name='detail'),
    path('edit/<int:pk>/', Update.as_view() , name='edit'),
    path('delete/<int:pk>/', Delete.as_view() , name='delete'),

]
