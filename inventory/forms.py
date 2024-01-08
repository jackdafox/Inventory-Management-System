from django import forms
from .models import Product, Inventory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name']
        labels = {
            "name": "Inventory Name",
        }