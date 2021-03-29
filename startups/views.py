from django.shortcuts import render, redirect
from . import models


def add_startup(request):
    if request.method == 'POST':
        form = models.AddStartupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = models.AddStartupForm()
    return render(request, 'add.html', {'form': form})
