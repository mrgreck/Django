from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context


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
    permission_required = ('NewsPaper.add_post',)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'NewsPaper/post_create.html'
    form_class = PostForm
    success_url = ''
    permission_required = ('NewsPaper.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'NewsPaper/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'
    permission_required = ('NewsPaper.delete_post',)


class CategoryList(ListView):
    model = Category
    template_name = 'NewsPaper/Category/category_list.html'
    context_object_name = 'Category'
    queryset = Category.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context


class CategoryCreate(CreateView):
    model = Category
    template_name = 'NewsPaper/Category/category_create.html'
    fields = ['name']


class CategoryDelete(DeleteView):
    template_name = 'NewsPaper/Category/delete.html'
    queryset = Category.objects.all()
    success_url = '/category'


class CategoryEdit(UpdateView):
    template_name = 'NewsPaper/Category/category_create.html'
    fields = ['name']
    success_url = ''

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Category.objects.get(pk=id)


class CategoryDetail(DetailView):
    model = Category
    template_name = 'NewsPaper/Category/detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context



@login_required
def followers_to_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.followers.add(request.user)
    category.save()

    return redirect('/')



