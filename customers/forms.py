from django import forms
from .models import Customer, SalesAdvisor, AdviserCustomer, Location

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AdviserCustomerForm(forms.ModelForm):
    class Meta:
        model = AdviserCustomer
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
