from django import forms
from .models import Dogovor, Payment


class DogovorForm(forms.ModelForm):
    class Meta:
        model = Dogovor
        fields = ('name', 'number', 'date', 'end_date', 'tel1', 'tel2', 'tel3', 'fiz', 'address_city', 'address_street',
                  'address_house', 'address_kv', 'equip', 'sum', 'discount', 'amount', 'comment', 'active')


