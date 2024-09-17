from django.contrib import admin
from .models import Medicine, Pharmacist
from .forms import PharmacistCreateForm

# Register your models here.

from .forms import MedicineCreateForm
class MedicineCreateForm(admin.ModelAdmin):
    display_list = [all]
    form = MedicineCreateForm
    list_filter = ['category']
    search_field = ['MedicineName']


class PharmacistCreateForm(admin.ModelAdmin):
    display_list = ['firstName', 'lastName','address', 'phone', 'added_on']
    form = PharmacistCreateForm
    list_filter = ['pharmacistName']
    search_field = ['id']


admin.site.register(Medicine, MedicineCreateForm)
admin.site.register(Pharmacist, PharmacistCreateForm)







