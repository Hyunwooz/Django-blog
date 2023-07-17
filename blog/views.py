from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm

### Post
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs
        }
        return render(request, 'blog/post_list.html', context)


class Write(View):
    
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request,'blog/post_write.html',context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_write.html',context)
    

class Detail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        if post.status == 'active':
            comments = Comment.objects.filter(post=post)
            comment_form = CommentForm()
            
            context = {
                'post': post,
                'comments': comments,
                'comment_form': comment_form,
            }
        
            return render(request,'blog/post_detail.html', context)
        
        return render(request,'blog/error.html')
    

class Update(View):
    def get(self, request, pk):
        
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content, 'category': post.category})
        context = {
            'form': form,
            'post': post,
        }
        return render(request, 'blog/post_edit.html', context)
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_edit.html', context)


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.status = 'delete'
        post.save()
        
        return redirect('blog:list')