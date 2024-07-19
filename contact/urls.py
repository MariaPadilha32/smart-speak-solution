from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactgeneral, name='contact general'),
    path('general/', views.contact, name='contact'),
    path('faq/', views.contactfaq, name='contactfaq'),
]
