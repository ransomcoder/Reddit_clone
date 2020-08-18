from django.shortcuts import render, redirect, get_object_or_404
from .models import Community
from .forms import CommunityForm


def community_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommunityForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.leader = request.user
                new_form.save()
                new_form.members.add(request.user)

            return redirect('home')
        form = CommunityForm()
        context = {
            'title': 'Create Community',
            'form': form
        }
        return render(request, 'community/community_create.html', context)
    else:
        return redirect('/login/?next=/community/create/')


def community_detail(request, pk):
    community = get_object_or_404(Community, id=pk)
    context = {
        'title': 'Community Detail',
        'community': community,
    }
    return render(request, 'community/community_detail.html', context)
