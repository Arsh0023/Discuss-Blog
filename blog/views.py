from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView,
    )
from blog.models import Post,Comments
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin #these are a kin to the decorator login required
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin , CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('blog:post_list')
    model = Post

class DraftListView(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')

###############################
###############################

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk) #now we have the model object
    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        if(form.is_valid()):
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    
    return(render(request,'blog/comment_form.html',{'form':form}))

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk = post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('blog:post_detail',pk = pk)    
