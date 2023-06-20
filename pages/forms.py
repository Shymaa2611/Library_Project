from django import forms
from .models import client_data

class ContactForm(forms.ModelForm):
    class Meta:
        model=client_data
        fields=[
            'name',
            'phone',
            'email',
            'message',
         ]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
          
            }