from startups.forms import AddStartupForm
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from startups import forms


def add_startup(request):
    if request.method == 'POST':
        form = AddStartupForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            detail = form.save(commit=False)
            detail.startup_user = request.user
            detail.save()
            # form.save()
            try:
                print(request.user)
                form.save()

            except Exception as e:
                print('\n\n\n')
                print(e)
            return redirect('home')

    else:
        form = AddStartupForm()
    return render(request, 'add.html', {'form': form})


def update_startup(request, str):
    obj = get_object_or_404(models.StartupModel, id=str,
                            startup_user=request.user)
    # print(f'\n\n\nobj {obj}')
    form = AddStartupForm(request.POST, instance=obj)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home')

    return render(request, 'update.html', {'form': form})


def view_startup(request, str):
    obj = models.StartupModel.objects.filter(id=str)
    return render(request, 'details.html', {'contents': obj})


def display_startup(request):
    # content = models.StartupModel.objects.all()
    content = models.StartupModel.objects.filter(startup_user=request.user)
    print(content)
    return render(request, 'view.html', {'contents': content})


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)


def delete_startup(request, str):
    obj = models.StartupModel.objects.filter(id=str).delete()
    return render(request, 'index.html')
