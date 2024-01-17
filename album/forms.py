from django import forms
from .import models




class Album(forms.ModelForm):
    class Meta:
        model = models.Album_models
        fields='__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }