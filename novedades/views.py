from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomeView(TemplateView):
    template_name = 'novedades/home.html'

class AboutView(TemplateView):
    template_name = 'novedades/about.html'

class BlogCafeListView(ListView):
    model = Post
    template_name = 'novedades/blog_list.html'
    context_object_name = 'posts'
    ordering = ['-fecha']

class PostDetailView(DetailView):
    model = Post
    template_name = 'novedades/post_detail.html'
