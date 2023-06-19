from django.shortcuts import render
from .models import Post
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.

def increase_view_count(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.view_count += 1
    post.save()
    # Render the template for the blog post view
    # ...

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

class NavContact(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'contact.html'

class NavHam(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'ham.html'

class NavAut(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'author.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        # Call the increase_view_count function
        increase_view_count(request, self.kwargs['slug'])
        return super().get(request, *args, **kwargs)


