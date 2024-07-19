from . import views
from django.urls import path
from .views import PostList
from .views import PostCreateView
from .views import UpdatePostView
from .views import DeletePostView


urlpatterns = [
    path('', views.PostList.as_view(), name="blog"),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path(
        'update_post/<slug:slug>',
        UpdatePostView.as_view(),
        name='update_post'
    ),
    path(
        'delete_post/<slug:slug>/delete',
        DeletePostView.as_view(),
        name='delete_post'
    ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
