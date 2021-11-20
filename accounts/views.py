from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-index')

    return render(request, 'registration/signup.html', context={'form': form})
