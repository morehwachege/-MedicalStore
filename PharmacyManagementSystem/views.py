from django.contrib import messages
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import csv
#import reportLab for PDF generation
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
from .models import*
from .forms import*
from .forms import  MedicineCreateForm, MedicineUpdateForm,CustomerUpdateForm, PharmacistCreateForm, MedicineSearchForm, MedicineUpdateForm,IssueMedicineCreateForm, ReceiveMedicineForm, medReorderLevelForm


# Create your views here.

#home page
def index(request):
    title = 'Welcome : this the home page'
    form = 'Welcome : this the home page'
    context ={
        "title": title,
        "test": form,
    }
    return render(request, "index.html", context)

#medicine list
def medList(request):
    title = ' Medicine'
    queryset = Medicine.objects.all()
    form =MedicineSearchForm(request.POST or None)
    context= {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
   
    if request.method =='POST':
        queryset = Medicine.objects.filter(category__icontains=form['category'].value(),
                                          MedicineName__icontains=form['MedicineName'].value())
        context= {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    return render(request, "medList.html", context)


def addMedicine(request):
    form = MedicineCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/medList')
    context ={
        "form": form,
        "title": "Add Medicine",
    }
    return render(request, "addMedicine.html", context)

    #view medicine details
def medicineDetail(request, pk):
    queryset = Medicine.objects.get(id=pk)
    context ={
        "title": queryset.MedicineName,
        "queryset": queryset,
    }
    return render(request, 'medicineDetail.html', context)

    #delete Medicine view
def deleteMedicine(request, pk):
    queryset = Medicine.objects.get(id = pk)
    if request.method =='POST':
       queryset.delete()
       messages.success(request, "Successfully Deleted!")
       return redirect('/medList')
    return render(request, 'deleteMedicine.html')

#Update Medicine
def MedicineUpdate(request, pk):
    queryset = Medicine.objects.get(id=pk)
    form = MedicineUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = MedicineUpdateForm(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
        return redirect('/medList')
    context ={
        "form":form,
        "title": "Update Item"
    }
    return render(request, 'addMedicine.html', context)

#Issue Medicine view
def IssueMedicine(request, pk):
    queryset = Medicine.objects.get(id = pk)
    form = IssueMedicineCreateForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.receiveQuantity = 0
        instance.quantity -= instance.issueQuantity
        instance.issueBy = str(request.user)
        messages.success(request, "Issued successfully." + str(instance.quantity) + " " + str(instance.MedicineName) +
         "s now left in store")
        instance.save()
        
        return redirect('/medicineDetail/'+str(instance.id))
        #return HttpResponseRedirect(instance.get_absolute_url())
    context={
            "title":'Issue'+ " " + str(queryset.MedicineName),
            "queryset": queryset,
            "form": form,
            "username":'Issued By:' + str(request.user),
        }
    return render(request, 'addMedicine.html', context)

#Receive Medicine
def ReceiveMedicine(request, pk):
    queryset = Medicine.objects.get(id=pk)
    form = ReceiveMedicineForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance =form.save(commit= False)
        instance.issueQuantity = 0
        instance.quantity += instance.receiveQuantity
        instance.ReceivedBy = str(request.user)
        messages.success(request, "Received successfully." + str(instance.quantity) + " " + str(instance.MedicineName) +
         " s now  in store")
        instance.save()

        return redirect('/medicineDetail/'+str(instance.id))
        #return HttpResponseRedirect(instance.get_absolute_url())
    context={
            "title":'Receive'+ " " + str(queryset.MedicineName),
            "queryset": queryset,
            "form": form,
            "username":'Received By:' + str(request.user),
        }
    return render(request, 'addMedicine.html', context)

    #medicine reorder level alert
def medReorderLevel(request, pk):
    queryset = Medicine.objects.get(id=pk)
    form = medReorderLevelForm(request.POST or None, instance = queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success( request, "Reorder level for" + str(instance.MedicineName) + "is updated to" + str(instance.reorderLevel))
        return redirect('/medList/')
    context ={
        "instance":queryset,
        "form": form,
    }
    return render(request, 'addMedicine.html', context)

#update customer record
def UpdateCustomer(request, pk):
    queryset = Customer.objects.get(id=pk)
    form = CustomerUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
        return redirect('/customerRecords')
    context ={
        "form":form,
        "title": "Update Item"
    }
    return render(request, 'registerCustomer.html', context)

#Delete Record
def deleteCustomer(request, pk):
    queryset = Customer.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return HttpResponseRedirect('/customerRecords')
    return render(request, 'deleteCustomer.html')

#Register Customers
#@login_required
def customerRecords(request):
    title = 'Customers'
    queryset = Customer.objects.all()
    context ={
        "title": title,
        "queryset":queryset,
    }
    return render(request, "customerRecords.html", context)
def registerCustomer(request):
    form = CustomerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/customerRecords')
    context ={
            "form": form,
            "title": "Register New Customer"
        }
    return render(request, "registerCustomer.html", context)

#pharmacist
def addPharmacist(request):
    form = PharmacistCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, "pharmacistRecord.html")
    context ={
        "form":form,
        "title": "Add Pharmacist To System"
    }
    return render(request, "pharmacist.html", context)

def pharmacistRecord(request):
    form = PharmacistCreateForm(request.POST or None)
    if form.is_valid():
       form.save()
    context ={
        "form": form,
        "title": "Pharmacists"
    }
    return redirect(request, "pharmacistRecord.html",context)

