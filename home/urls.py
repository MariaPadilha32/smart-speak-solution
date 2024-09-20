from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('subscribe', views.subscribe, name='subscribe'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
]
