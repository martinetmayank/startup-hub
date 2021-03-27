from django.forms import ModelForm
from . forms import AddForm


class AddStartupForm(ModelForm):
    class Meta:
        model = AddForm
        # fields = ('name', 'email')
        fields = '__all__'
