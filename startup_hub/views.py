from django.shortcuts import render
from startups import forms, models


def home(request):
    contents = models.StartupModel.objects.all()
    # print(content)
    return render(request, 'index.html', {'contents': contents})
