from csv import writer
from django.shortcuts import render, redirect
from Customers.models import Customer
from Customers.forms import CustomerCreateForm, CustomerUpdateForm
from django.http import HttpResponse, response
import csv

# Create your views here.
#Register Customers
#@login_required
def customerRecords(request):
    title = 'Customers'
    customer = Customer.objects.all()
    context ={
        "title": title,
        "customers":customer,
    }
    return render(request, "customers/customerRecords.html", context)
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
    return render(request, 'customers/registerCustomer.html', context)

    #view single customer record
def customer_detailView(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={
        "title": customer.firstName,
        "customer": customer,
    }
    return render(request, 'customers/customer_detail.html', context)

#Delete Record
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customerRecords')
    context={'customer':customer}
    return render(request, 'customers/deleteCustomer.html', context)

#generate Report
def Customer_report(request):
    response= HttpResponse(content_type='text/csv')
    response['content-Disposition']= 'attachment; filename= CustomerReport.csv'
    #create a csv Writer
    writer= csv.writer(response)
    #Designate the model
    customers = Customer.objects.all()
    #add column heading to the csv file 
    writer.writerow(['First Name', 'Last Name', 'Address', 'Phone'])
    #Loop Through the customers object and output
    for customer in customers:
        writer.writerow([customer.firstName, customer.lastName, customer.address, customer.contact])
    return response


