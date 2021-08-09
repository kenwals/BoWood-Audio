from django.urls import path
from . import views

urlpatterns = [
    path('add/review/<int:product_id>/', views.add_review, name='add_review'),
    path('edit/review/<int:review_id>/', views.edit_review, name='edit_review'),
]
