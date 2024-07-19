from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path("profile_update/", views.profile_update, name="profile_update"),
    path(
        'profile_delete/<int:pk>/',
        views.profile_delete,
        name='profile_delete'
    ),
]
