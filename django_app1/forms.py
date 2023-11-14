from .models import Character
from django import forms
from django.forms import ModelForm, TextInput


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "href"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "href": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter href'
            }),
        }


class FindCharForm(forms.Form):
    input_name = forms.CharField(max_length=100)
