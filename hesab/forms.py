from django import forms

from .models import Week, Shopping, Money


class MoneyForm(forms.Form):
    # class Meta:
    #     model = Money
    #     fields = ['user', 'week', 'money']

    user = forms.Select()
    week = forms.Select()
    money = forms.IntegerField()

