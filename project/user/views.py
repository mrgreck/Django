from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from NewsPaper.models import Author
from .forms import BaseRegisterForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/user'


class EditUser(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['username']
    success_url = '/user'


@login_required
def upgrade_me(request):
    user = request.user
    authors = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors.user_set.add(user)
        Author.objects.create(user=user)
    return redirect('/user')
