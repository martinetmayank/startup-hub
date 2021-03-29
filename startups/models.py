from django import forms
from django.forms import ModelForm, widgets
from . forms import AddForm


class AddStartupForm(ModelForm):
    class Meta:
        model = AddForm
        # fields = ('name', 'email')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'startup-name'}),
            'description': forms.Textarea(attrs={'class': 'startup-description'}),
            'email': forms.EmailInput(attrs={'class': 'startup-email'}),
            'awards': forms.Textarea(attrs={'class': 'startup-awards'}),
            'youtube': forms.TextInput(attrs={'class': 'startup-youtube'}),
            'linkedin': forms.TextInput(attrs={'class': 'startup-linkedin'}),
            'twitter': forms.TextInput(attrs={'class': 'startup-twitter'}),
            'facebook': forms.TextInput(attrs={'class': 'startup-facebook'}),
            'instagram': forms.TextInput(attrs={'class': 'startup-instagram'}),
            'location': forms.TextInput(attrs={'class': 'startup-location'}),
        }
