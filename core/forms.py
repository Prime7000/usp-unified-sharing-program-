from django import forms
from .models import data, label
from django.forms import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class dataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ['file']
        widgets = {
            'file': MultipleFileInput()
        }