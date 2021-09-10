from django import forms
from .models import WorkOrder


class OrderForm(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = '__all__'

