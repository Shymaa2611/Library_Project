from django import forms
from .models import books,Category


class BookForm(forms.ModelForm):
    class Meta:
        model=books
        fields=[
            'title',
            'authorname',
            'number_of_pages',
            'price',
            'status',
            'book_category'
        ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'authorname':forms.TextInput(attrs={'class':'form-control'}),
            'number_of_pages':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'book_category':forms.Select(attrs={'class':'form-control'}),
            
            }
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'name'
        ]
        widgets={'name':forms.TextInput(attrs={'class':'form-control'})}

