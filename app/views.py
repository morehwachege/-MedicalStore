from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import csv
from django.db.models import Sum
from .models import Medicine, Customers, Order
# from .forms import*
from .forms import  MedicineCreateForm, CustomerCreateForm,MedicineSearchForm,CustomerUpdateForm, MedicineUpdateForm, PharmacistCreateForm,IssueMedicineCreateForm, ReceiveMedicineForm, medReorderLevelForm, OrderCreateForm, OrderUpdateForm
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from xhtml2pdf import pisa


#medicine list
@login_required(login_url='login')    
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
    return render(request, "pharmacy/medList.html", context)

@login_required(login_url='login')    
def addMedicine(request):
    form = MedicineCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/medList')
    context ={
        "form": form,
        "title": "Add Medicine",
    }
    return render(request, "pharmacy/addMedicine.html", context)

    #view medicine details
@login_required(login_url='login')    
def medicineDetail(request, pk):
    queryset = Medicine.objects.get(id=pk)
    context ={
        "title": queryset.MedicineName,
        "queryset": queryset,
    }
    return render(request, 'pharmacy/medicineDetail.html', context)

    #delete Medicine view
@login_required(login_url='login')    
def deleteMedicine(request, pk):
    queryset = Medicine.objects.get(id = pk)
    if request.method =='POST':
       queryset.delete()
       messages.success(request, "Successfully Deleted!")
       return redirect('/medList')
    return render(request, 'pharmacy/deleteMedicine.html')

#Update Medicine
@login_required(login_url='login')    
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
    return render(request, 'pharmacy/addMedicine.html', context)

#Issue Medicine view
@login_required(login_url='login')    
def IssueMedicine(request, pk):
    queryset = Medicine.objects.get(id = pk)
    form = IssueMedicineCreateForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.receiveQuantity = 0
        instance.quantity -= instance.issueQuantity
        if instance.issueQuantity > queryset.quantity:
            messages.info(request, "there isn't enough Quantity in store to issue" + str(instance.issueQuantity))
            instance.issueBy = str(request.user)
        else:
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
    return render(request, 'pharmacy/addMedicine.html', context)

#Receive Medicine
@login_required(login_url='login')    
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
    return render(request, 'pharmacy/addMedicine.html', context)

    #medicine reorder level alert
@login_required(login_url='login')    
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
    return render(request, 'pharmacy/addMedicine.html', context)

#Generate Medicine Report(CSV) 
@login_required(login_url='login')    
def Medicine_Report(request):
    response = HttpResponse(content_type='text/csv')
    response['content-Disposition']= 'attachment; filename=medicineReport.csv'
    #Create a csv Writer
    writer= csv.writer(response)
    #Designate the Model
    medicines = Medicine.objects.all()
    #adding column  heading to the csv file 
    writer.writerow(['MedicineName','category ','quantity', 'amount', 'reorderLevel', 'lastUpdated','added_on'])
    #loop Through the Medicine and Output
    for medicine in medicines:
        writer.writerow([medicine.MedicineName,medicine.category, medicine.quantity, medicine.amount, medicine.reorderLevel, medicine.lastUpdated,medicine.added_on])          
    return response

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

#Register Customers
#@login_required
@login_required(login_url='login')   
def customerRecords(request):
    title = 'Customers'
    customer = Customers.objects.all()
    context ={
        "title": title,
        "customers":customer,
    }
    return render(request, "customers/customerRecords.html", context)

@login_required(login_url='login')   
def registerCustomer(request):
    form = CustomerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customerRecords')
    context ={
            "form": form,
            "title": "Register New Customer"
        }
    return render(request, "customers/registerCustomer.html", context)

#update customer record
@login_required(login_url='login')   
def UpdateCustomer(request, pk):
    queryset = Customers.objects.get(id=pk)
    form = CustomerUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
        return redirect('/customerRecords')
    context ={
        "form":form,
        "title": "Update" + " "+ queryset.firstname
    }
    return render(request, 'customers/registerCustomer.html', context)

    #view single customer record
@login_required(login_url='login')      
def customer_detailView(request, pk):
    customer = Customers.objects.get(id=pk)
    orders=customer.order_set.all()
    context ={
        "title": customer.firstname,  
        "customer": customer,
        'orders':orders,
    }
    return render(request, 'customers/customer_detail.html', context)

#Delete Record
@login_required(login_url='login')   
def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customerRecords')
    context={'customer':customer}
    return render(request, 'customers/deleteCustomer.html', context)

#generate Report
@login_required(login_url='login')   
def Customer_report(request):
    response= HttpResponse(content_type='text/csv')
    response['content-Disposition']= 'attachment; filename= CustomerReport.csv'
    #create a csv Writer
    writer= csv.writer(response)
    #Designate the model
    customers = Customers.objects.all()
    #add column heading to the csv file 
    writer.writerow(['First Name', 'Last Name', 'Address', 'Phone'])
    #Loop Through the customers object and output
    for customer in customers:
        writer.writerow([customer.firstname, customer.lastname, customer.address, customer.contact])
    return response

def create_order(request):
    form = OrderCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders')
    context ={
            "form": form,
            "title": "Create New Order"
        }
    return render(request, "orders/create_order.html", context)

# @login_required(login_url='login')   
def orders_view(request):
    title = 'Sales'
    orders = Order.objects.all()
    sales = Order.objects.all().aggregate(total_sales=Sum('total_price'))
    context ={
        "title": title,
        "orders":orders,
        "sales":sales,
    }
    return render(request, "orders/orders.html", context)

# #update customer record
# @login_required(login_url='login')   
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderUpdateForm(instance = order)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
        return redirect('orders')
    context ={
        "form":form,
        "title": "Update Item"
    }
    return render(request, 'orders/create_order.html', context)

 #Delete Record
@login_required(login_url='login')   
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('customerRecords')
    context={'order':order}
    return render(request, 'orders/delete_order.html', context)

#generate receipt
def print_receipt(request, pk):
    orders=Order.objects.get(id=pk)
    template_path = 'orders/receipt.html'
    
    context={
        'orders':orders,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
  
# generate Report
@login_required(login_url='login')   
def order_report(request):
    response= HttpResponse(content_type='text/csv')
    response['content-Disposition']= 'attachment; filename= CustomerReport.csv'
    #create a csv Writer
    writer= csv.writer(response)
    #Designate the model
    orders = Order.objects.all()
    #add column heading to the csv file 
    writer.writerow(['Customer Name', 'Medicine', 'Quantity', 'Price', 'Total Price', 'Date'])
    #Loop Through the customers object and output
    for order in orders:
        writer.writerow([order.customer, order.medicne, order.price, order.total_price, order.date])
    return response

