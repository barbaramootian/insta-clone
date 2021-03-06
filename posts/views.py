
from posts.models import Post
from posts.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context
        
class PostFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'posts'
