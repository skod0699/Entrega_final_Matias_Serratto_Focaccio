from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomeView(TemplateView):
    template_name = 'novedades/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(destacado=True).order_by('-fecha')[:3]
        return context

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
