from django import forms
from .models import TransactionModel


class DepositeForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount']