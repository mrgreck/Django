from django.urls import path
from .views import PostList,PostDetail,PostSearch,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(),name='news_d'),
    path('search/', PostSearch.as_view(),name='search'),
    path('add/', PostCreateView.as_view(),name='AddPost'),
    path('edit/<int:pk>/', PostUpdateView.as_view(),name='EditPost'),
    path('delete/<int:pk>/', PostDeleteView.as_view(),name='DeletePost'),
]