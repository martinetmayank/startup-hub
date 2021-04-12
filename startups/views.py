from startups.forms import AddStartupForm
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from startups import forms


def add_startup(request):
    if request.method == 'POST':
        form = AddStartupForm(request.POST)
        if form.is_valid():
            # form.save()
            try:
                form.save()
            except Exception as e:
                print('\n\n\n')
                print(e)
            return redirect('home')

    else:
        form = AddStartupForm()
    return render(request, 'add.html', {'form': form})


def update_startup(request, str):
    obj = get_object_or_404(models.StartupModel, uid=str)
    # print(f'\n\n\nobj {obj}')
    form = AddStartupForm(request.POST, instance=obj)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home')

    return render(request, 'update.html', {'form': form})


def view_startup(request, str):
    obj = models.StartupModel.objects.filter(uid=str)
    return render(request, 'details.html', {'contents': obj})


def display_startup(request):
    content = models.StartupModel.objects.all()
    print(content)
    return render(request, 'view.html', {'contents': content})


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)
