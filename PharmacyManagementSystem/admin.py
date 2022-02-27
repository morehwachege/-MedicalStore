from django.contrib import admin
from .models import Medicine, Customer, Pharmacist


# Register your models here.

from .forms import MedicineCreateForm
class MedicineCreateForm(admin.ModelAdmin):
    display_list = [all]
    form = MedicineCreateForm
    list_filter = ['category']
    search_field = ['MedicineName']

from .forms import PharmacistCreateForm
class PharmacistCreateForm(admin.ModelAdmin):
    display_list = ['firstName', 'lastName','address', 'phone', 'added_on']
    form = PharmacistCreateForm
    list_filter = ['pharmacistName']
    search_field = ['id']

from .forms import CustomerCreateForm
class CustomerCreateForm(admin.ModelAdmin):
    display_list = ['firstName','lastName', 'address', 'contact' 'added_on']
    form = CustomerCreateForm
    search_field = ['id']



admin.site.register(Medicine, MedicineCreateForm)
admin.site.register(Customer, CustomerCreateForm)
admin.site.register(Pharmacist, PharmacistCreateForm)







