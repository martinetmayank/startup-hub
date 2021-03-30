from django.shortcuts import render
from startups import forms


def home(request):
    contents = forms.AddForm.objects.all()
    # print(content)
    return render(request, 'index.html', {'contents': contents})
