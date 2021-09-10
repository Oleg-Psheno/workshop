from django import forms
from mainapp.models import Order

class MainForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ('user','phone')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['phone'].widget.attrs['placeholder'] = 'Введите номер телефона'
        self.fields['phone'].widget.attrs['data-tel-input'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-border-2 u-border-white u-input u-input-rectangle u-radius-50 u-white'