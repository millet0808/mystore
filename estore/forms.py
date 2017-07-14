from django import forms
from .models import Product
from .models import OrderInfo


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'quantity', 'price')


class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['billing_name', 'billing_address', 'shipping_name', 'shipping_address']
