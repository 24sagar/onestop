from django import forms
from .models import UserAddress

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'zip_code': forms.TextInput(attrs={'class': 'input', 'placeholder': 'ZIP Code'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Telephone'}),
        }

