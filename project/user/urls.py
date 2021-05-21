from django.urls import path, include
from .views import ProfileView, BaseRegisterView, EditUser, upgrade_me
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('signup/', BaseRegisterView.as_view(template_name='user/signup.html'), name='signup'),
    path('edit/<int:pk>/', EditUser.as_view(template_name='user/edit.html'), name='EditUser'),
    path('GiveAuthor/', upgrade_me, name='GiveAuthor'),
]