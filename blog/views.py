from django.shortcuts import render, redirect
from django.http import JsonResponse 
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, F
from .models import Post, Comment, ImageUpload, Category
from .forms import PostForm, CommentForm

### Post
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all().filter(status='active').order_by('-created_at')
        categories = Category.objects.filter(status='active').values('name').annotate(count=Count('name'),category=F('name')).values('count', 'category')
        context = {
            "posts": post_objs,
            "categories": categories,
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
        thumbnail = request.POST['thumbnail']
        category = request.POST['category']
        
        if thumbnail != "blank":
            post = Post.objects.create(title=title, content=content, writer=user,thumbnail=thumbnail)
        else:
            post = Post.objects.create(title=title, content=content, writer=user)
        category = Category.objects.create(post=post,name=category)
        
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
        category = Category.objects.get(post=post)
        
        post.title = request.POST['title']
        post.content = request.POST['content']
        thumbnail = request.POST['thumbnail']
        category.name = request.POST['category']
        
        if thumbnail != "blank":
            post.thumbnail = thumbnail
            
        post.save()
        category.save()
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
            'category': post.category.name,
            'thumbnail': str(post.thumbnail)
        }
        return JsonResponse(data)


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        if post.writer != request.user:
            return redirect('blog:list')
        category = Category.objects.get(post=post)
        
        post.status = 'delete'
        category.status = 'delete'
        
        category.save()
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
        post_objs = Post.objects.filter(status='active',title__contains=request.GET['keyword']).order_by('-created_at')
        categories = Category.objects.filter(status='active').values('name').annotate(count=Count('name'),category=F('name')).values('count', 'category')
        context = {
            "posts": post_objs,
            "categories": categories,
            "keyword": request.GET['keyword']
        }
        return render(request, 'blog/post_search.html', context)


class CategorySearch(View):
    def get(self, request):
        
        # print(results.query) SQL 쿼리문을 볼 수 있다.
        results = Category.objects.select_related().filter(name=request.GET['category'],status='active').order_by('-created_at')
        categories = Category.objects.filter(status='active').values('name').annotate(count=Count('name'),category=F('name')).values('count', 'category')
        context = {
            "results": results,
            "categories": categories,
            "keyword": request.GET['category']
        }
        return render(request, 'blog/post_category.html', context)

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
        
        if request.user != comment.writer:
            return render(request,'blog/error.html')
        
        post_id = comment.post.id
        comment.status = 'delete'
        comment.save()
    
        return redirect('blog:detail', pk=post_id)
    
        
    