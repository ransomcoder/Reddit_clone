from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.community_create, name='community_create'),
    path('<str:pk>', views.community_detail, name='community_detail'),
    # path('<str:pk>/edit', views.community_edit, name='community_edit'),
]
