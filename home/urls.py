from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('whatwedo/', views.whatwedo, name='whatwedo'),
]
