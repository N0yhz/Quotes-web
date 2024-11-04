from django.forms import ModelForm, CharField, TextInput
from django import forms
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = CharField(max_length=70, required=True, widget=TextInput())
    born_location = CharField(max_length=200, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['name','born_date','born_location','description']

class QuotesForm(ModelForm):

    quote = forms.CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=True)
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(),required=False, widget=forms.CheckboxSelectMultiple )

    class Meta:
        model = Quote
        fields = ['quote','author', 'tags']
