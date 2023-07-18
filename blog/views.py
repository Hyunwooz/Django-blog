from django.shortcuts import render, redirect
from django.http import JsonResponse 
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, ImageUpload
from .forms import PostForm, CommentForm

### Post
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all().filter(status='active').order_by('-created_at')
        categories = ['Life','Style','Tech','Sport','Photo','Develop','Music']
        context = {
            "posts": post_objs,
            "categories": categories
        }
        return render(request, 'blog/post_list.html', context)


class Write(LoginRequiredMixin, View):
    Mixin : LoginRequiredMixin
    login_url = '/user/login'
    redirect_field_name = 'next'
    
    def get(self, request):
            
        form = PostForm()
        context = {
            'form': form
        }
        return render(request,'blog/post_write.html',context)
    
    def post(self, request):

        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        thumbnail = request.POST['thumbnail']
        
        if thumbnail != "blank":
            post = Post.objects.create(title=title, content=content, category=category, writer=user,thumbnail=thumbnail)
        else:
            post = Post.objects.create(title=title, content=content, category=category, writer=user)

        # serializer = PostSerializer(post)
        data = {
            'message': '저장이 완료되었습니다.'
        }
        return JsonResponse(data)

class Detail(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return render(request,'blog/error.html')
        else:
            if post.status == 'active':
                post.views = post.views + 1
                post.save()
                
                comments = Comment.objects.filter(post=post,status='active')
                comment_form = CommentForm()
                
                context = {
                    'post': post,
                    'comments': comments,
                    'comment_form': comment_form,
                }
            
                return render(request,'blog/post_view.html', context)
        
            return render(request,'blog/error.html')
    

class Update(LoginRequiredMixin, View):
    Mixin : LoginRequiredMixin
    login_url = '/user/login'
    redirect_field_name = 'next'
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.writer == request.user:
            return render(request, 'blog/post_edit.html')
        return redirect('blog:list', pk=pk)
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        data = {
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'thumbnail': str(post.thumbnail)
        }
        return JsonResponse(data)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        # title = request.POST['title']
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        
        thumbnail = request.POST['thumbnail']
        
        if thumbnail != "blank":
            post.thumbnail = thumbnail
        
        post.save()
        # serializer = PostSerializer(post)
        data = {
            'message': '수정이 완료되었습니다.'
        }
        return JsonResponse(data)


class LoadPost(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        data = {
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'thumbnail': str(post.thumbnail)
        }
        return JsonResponse(data)


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.status = 'delete'
        post.save()
        
        return redirect('blog:list')


class ImgUpload(View):
    def post(self, request):
        image = request.FILES['image']
        imageUpload = ImageUpload.objects.create(image=image)
        url = imageUpload.image
        data = {
            'url': str(url)
        }
        return JsonResponse(data)


class Search(View):
    def get(self, request):
        post_objs = Post.objects.all().filter(status='active',title__contains=request.GET['keyword']).order_by('-created_at')
        context = {
            "posts": post_objs,
        }
        return render(request, 'blog/post_search.html', context)
    
    
### Comment
class CommentWrite(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        
        if form.is_valid():
            
            content = form.cleaned_data['content']    
            writer = request.user
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            
            return redirect('blog:detail', pk=pk)
        
        form.add_error(None,'폼이 유효하지 않습니다.')
        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'comment_form': form,
        }
        
        return render(request, 'blog/post_detail.html', context)
    
    
class CommentDelete(View):
    def post(self, request, pk):
        
        comment = Comment.objects.get(pk=pk)
        
        if request.user == comment.writer:
            post_id = comment.post.id
            comment.status = 'delete'
            comment.save()
        
            return redirect('blog:detail', pk=post_id)
        
        return render(request,'blog/error.html')
    