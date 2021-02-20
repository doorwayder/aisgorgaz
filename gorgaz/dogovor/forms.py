from django import forms
from .models import Dogovor, Payment


class SearchForm(forms.Form):
    query = forms.CharField()
