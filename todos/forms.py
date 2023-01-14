from django import forms
from .models import *


class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=29, widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Enter your task...', 'type': 'search'}))

    class Meta:
        model = Todo
        fields = ['title']
