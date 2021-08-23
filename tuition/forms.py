from django.forms import fields
from tuition.models import Contact
from django import forms
from .models import Contact
class CantactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
    
           