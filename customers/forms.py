from django import forms
from .models import Customer, AdviserCustomer, Location


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'sales_advisor', 'person_type', 'identification', 'name', 'last_name', 
            'company_name', 'trade_name', 'email', 'phone', 'principal_address',
            'mode', 'rut'
        ]
        widgets = {
            'sales_advisor': forms.Select(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'person_type': forms.Select(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'identification': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'company_name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'trade_name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'phone': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'principal_address': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'mode': forms.Select(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'rut': forms.FileInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
        }


class AdviserCustomerForm(forms.ModelForm):
    class Meta:
        model = AdviserCustomer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'phone': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        return phone

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'city': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
            'address': forms.TextInput(attrs={'class': 'block w-full border border-gray-300 bg-white rounded-md p-2'}),
        }
