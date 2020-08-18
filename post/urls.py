from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('<str:pk>', views.post_detail, name='post_detail'),
]
