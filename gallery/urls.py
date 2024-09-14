# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    # path('upload/', views.new_photo, name='new_photo'),
    # path('edit/<int:pk>/', views.edit_photo, name='edit_photo'),
    # path('delete/<int:pk>/', views.delete_photo, name='delete_photo'),
]
