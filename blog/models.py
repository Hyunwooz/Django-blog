from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default='active', max_length=20)
    category = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to='blog/media',null=True,blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default='active', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment on {self.post.title}'
    
### 이미지 업로드 모델
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='blog/media',null=True)
    created_at = models.DateTimeField(auto_now_add=True)