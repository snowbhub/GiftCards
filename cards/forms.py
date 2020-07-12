from django import forms
from . import models
from .models import Card


class CreateCards(forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ['series', 'number', 'expiration_date', 'date_of_use', 'amount', 'status', 'model_photo',]
        #expiration_date = forms.DateField(input_formats=['%d/%m/%Y'])