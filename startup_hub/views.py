from django.db.models.query_utils import Q
from django.shortcuts import render
from startups import forms, models


def home(request):
    contents = models.StartupModel.objects.all()
    # print(content)
    return render(request, 'index.html', {'contents': contents})


def search(request):
    search = request.GET['search']
    result = models.StartupModel.objects.filter(
        Q(description__icontains=search) | Q(name__icontains=search)
    )

    print(f'\n\nresult, {result}')
    return render(request, 'search.html', {'contents': result})
