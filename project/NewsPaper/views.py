from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post

from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1


class PostDetail(DetailView):
    model = Post
    template_name = 'NewsPaper/news_d.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'NewsPaper/search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'NewsPaper/post_create.html'
    form_class = PostForm
    permission_required = ('newspaper.add_post',)


class PostUpdateView(PermissionRequiredMixin, UpdateView ):
    template_name = 'NewsPaper/post_create.html'
    form_class = PostForm
    success_url = ''
    permission_required = ('newspaper.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'NewsPaper/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'
    permission_required = ('newspaper.delete_post',)