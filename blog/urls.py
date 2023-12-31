from django.urls import path
from .views import Index, Write, Detail, Delete, Update, CommentWrite, CommentDelete, Search, ImgUpload, LoadPost, CategorySearch, Likepost

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view() , name='list'),
    # post
    path('write/', Write.as_view() , name='write'),
    path('<int:pk>/', Detail.as_view() , name='detail'),
    path('edit/<int:pk>/', Update.as_view() , name='edit'),
    path('loadpost/<int:pk>/', LoadPost.as_view() , name='load'),
    path('delete/<int:pk>/', Delete.as_view() , name='delete'),
    path('search/', Search.as_view() , name='search'),
    path('categorysearch/', CategorySearch.as_view() , name='category'),
    path('imageupload/', ImgUpload.as_view() , name='img-upload'),
    path('like/<int:pk>/', Likepost.as_view() , name='like'),
    # comment
    path('comment/write/<int:pk>/', CommentWrite.as_view() , name='cm-write'),
    path('comment/delete/<int:pk>/', CommentDelete.as_view() , name='cm-delete'),

]
