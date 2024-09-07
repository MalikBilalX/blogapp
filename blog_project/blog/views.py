from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class BlogsListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'blog_detail'
