from django import forms
from .models import Cashiering

class CasheringForm(forms.ModelForm):
    class Meta:
        model = Cashiering
        fields = ['id', 'items']

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'items': forms.Select(attrs={'class': 'form-control', 'id': 'items list'})
        }

