from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=128, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': ('Username'), 'class': 'usernanme'})

        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('first name'), 'class': 'f_name'})

        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('last name'), 'class': 'l_name'})

        self.fields['email'].widget.attrs.update(
            {'placeholder': ('Email'), 'class': 'email'})

        self.fields['password1'].widget.attrs.update(
            {'placeholder': ('Password'), 'class': 'password1'})

        self.fields['password2'].widget.attrs.update(
            {'placeholder': ('Repeat password'), 'class': 'password2'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
