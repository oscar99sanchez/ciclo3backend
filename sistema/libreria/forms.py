from django import forms
from .models import Mouses

class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouses
        fields = '__all__'
