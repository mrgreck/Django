from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreateView, PostUpdateView,\
    PostDeleteView, CategoryList, CategoryCreate, CategoryEdit, CategoryDelete,\
    CategoryDetail, followers_to_category

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='news_d'),
    path('search/', PostSearch.as_view(), name='search'),
    path('add/', PostCreateView.as_view(), name='AddPost'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='EditPost'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='DeletePost'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/create', CategoryCreate.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryEdit.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    path('category/detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/followers_to_category/', followers_to_category),
]
