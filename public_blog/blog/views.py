from django.shortcuts import redirect, render
from blog.models import post, comment
from django.utils import timezone
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = post

    def get_queryset(self):
        return post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = post

    def get_queryset(self):
        return post.objects.filter(publish_date__isnull=True).order_by('create_date')