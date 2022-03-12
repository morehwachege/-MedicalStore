from django import forms
from .models import*


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['category', 'MedicineName', 'quantity', 'reorderLevel']
#validate category
        def clean_category(self):
            category = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError('this field is required')
            for instance in Medicine.objects.all():
                    if instance.category == category:
                        raise forms.ValidationError(category + 'already exists!')
            return category
            
#validate medicine name
        def clean_medicine(self):
            MedicineName = self.cleaned_data.get('MedicineName')
            if not MedicineName:
                raise forms.ValidationError('this field is required')

#search Medicine
class MedicineSearchForm(forms.ModelForm):
    Export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Medicine
        fields =['category', 'MedicineName']

#Update Medicine
class MedicineUpdateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['category', 'MedicineName', 'quantity']

#Issue Medicine
class IssueMedicineCreateForm(forms.ModelForm):
    class Meta:
        model =Medicine
        fields = [ 'issueQuantity', 'issueTo']

#Receive Medicine
class ReceiveMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['receiveQuantity', 'receivedBy']

class medReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['reorderLevel']

class PharmacistCreateForm(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = ['id', 'pharmacistName',  'address', 'phone', 'added_on']