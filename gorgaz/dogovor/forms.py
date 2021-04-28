from django import forms
from .models import Dogovor, Payment, Order


class DogovorForm(forms.ModelForm):
    class Meta:
        model = Dogovor
        fields = ('name', 'number', 'date', 'end_date', 'tel1', 'tel2', 'tel3', 'fiz', 'address_city', 'address_street',
                  'address_house', 'address_kv', 'equip', 'sum', 'discount', 'amount', 'comment', 'active',
                  'created_by', 'terminate_date', )


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
