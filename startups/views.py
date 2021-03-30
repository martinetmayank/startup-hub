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


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)
