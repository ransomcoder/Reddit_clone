from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post_form = form.save(commit=False)
                post_form.user = request.user
                post_form.save()

            return redirect('home')
        form = PostForm()
        context = {
            'title': 'Create Post',
            'form': form
        }
        return render(request, 'post/post_create.html', context)
    else:
        return redirect('/login/?next=/post/create/')


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {
        'title': 'Post Detail',
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)
