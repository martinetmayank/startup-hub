from django import forms
from django.forms import ModelForm
from . models import StartupModel


class AddStartupForm(ModelForm):
    class Meta:
        model = StartupModel
        fields = '__all__'
        exclude = ('startup_user', 'date_added',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'startup-name'}),
            'description': forms.Textarea(attrs={'class': 'startup-description', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'startup-email'}),
            'awards': forms.Textarea(attrs={'class': 'startup-awards'}),
            'youtube': forms.TextInput(attrs={'class': 'startup-youtube'}),
            'location': forms.TextInput(attrs={'class': 'startup-location'}),
        }
