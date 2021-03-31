from startups.forms import AddForm
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from startups import forms


def add_startup(request):
    if request.method == 'POST':
        form = models.AddStartupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = models.AddStartupForm()
    return render(request, 'add.html', {'form': form})


def update_startup(request, id):
    obj = get_object_or_404(AddForm, id=id)
    form = models.AddStartupForm(request.POST, instance=obj)

    # if request.method == 'POST':
    #     new_instance = AddForm
    #     form = models.AddStartupForm(instance=new_instance, data=request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('home')

    return render(request, 'update.html', {'form': form})


def view_startup(request, id):
    obj = forms.AddForm.objects.filter(id=id)
    return render(request, 'details.html', {'contents': obj})


def display_startup(request):
    content = forms.AddForm.objects.all()
    print(content)
    return render(request, 'view.html', {'contents': content})


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)
