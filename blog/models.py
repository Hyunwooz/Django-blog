from django.db import models

# Create your models here.
class Post(models.Model):
    
    CATEGORY_1 = "T1"
    CATEGORY_2 = "T2"
    CATEGORY_CHOICES = ((CATEGORY_1, "Test1"), (CATEGORY_2, "Test2"))
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='active')
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment on {self.post.title}'