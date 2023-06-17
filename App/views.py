from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class NavB(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'book.html'

class NavF(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'film.html'

class NavG(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'general.html'







