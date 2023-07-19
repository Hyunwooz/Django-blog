from django.contrib import admin
from .models import Post, Comment, ImageUpload, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ImageUpload)
admin.site.register(Category)