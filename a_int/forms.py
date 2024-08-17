from django import forms
from .models import Product, Item

class ProdForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['item_id']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'price': forms.NumberInput(attrs={'placeholder': 'price'}),
            'color': forms.TextInput(attrs={'placeholder': 'color'}),
            'size': forms.NumberInput(attrs={'placeholder': 'size'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'number in stock'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['product'].queryset = Product.objects.filter(business__administrator=user)