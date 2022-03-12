from django import forms
from Customers.models import Customer

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'lastName', 'contact', 'address']
class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= "__all__"
