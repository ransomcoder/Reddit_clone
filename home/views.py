from django.shortcuts import render
from post.models import Post


def home(request):
    posts = Post.objects.all()

    context = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'home/home.html', context)
