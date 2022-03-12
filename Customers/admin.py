from django.contrib import admin
from Customers.models import Customer
from Customers.forms import CustomerCreateForm

# Register your models here.
from .forms import CustomerCreateForm
class CustomerCreateForm(admin.ModelAdmin):
    display_list = ['firstName','lastName', 'address', 'contact' 'added_on']
    form = CustomerCreateForm
    search_field = ['id']

admin.site.register(Customer, CustomerCreateForm)