from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogsListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'blog_detail'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = ['title', 'author', 'body']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')