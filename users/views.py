from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UserRegistrationForm()
        context = {'title': 'Register', 'form': form}
        return render(request, 'users/register.html', context)
    else:
        return redirect('home')
