# from csv import writer
# from django.shortcuts import render, redirect
# from Customers.models import Customers
# from Customers.forms import CustomerCreateForm, CustomerUpdateForm
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, response
# import csv

# # Create your views here.
# #Register Customers
# #@login_required
# @login_required(login_url='login')   
# def customerRecords(request):
#     title = 'Customers'
#     customer = Customers.objects.all()
#     context ={
#         "title": title,
#         "customers":customer,
#     }
#     return render(request, "customers/customerRecords.html", context)

# @login_required(login_url='login')   
# def registerCustomer(request):
#     form = CustomerCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('customerRecords')
#     context ={
#             "form": form,
#             "title": "Register New Customer"
#         }
#     return render(request, "customers/registerCustomer.html", context)

# #update customer record
# @login_required(login_url='login')   
# def UpdateCustomer(request, pk):
#     queryset = Customers.objects.get(id=pk)
#     form = CustomerUpdateForm(instance = queryset)
#     if request.method == 'POST':
#         form = CustomerUpdateForm(request.POST, instance = queryset)
#         if form.is_valid():
#             form.save()
#         return redirect('/customerRecords')
#     context ={
#         "form":form,
#         "title": "Update Item"
#     }
#     return render(request, 'customers/registerCustomer.html', context)

#     #view single customer record
# @login_required(login_url='login')      
# def customer_detailView(request, pk):
#     customer = Customers.objects.get(id=pk)
#     context ={
#         "title": customer.firstname,  
#         "customer": customer,
#     }
#     return render(request, 'customers/customer_detail.html', context)

# #Delete Record
# @login_required(login_url='login')   
# def deleteCustomer(request, pk):
#     customer = Customers.objects.get(id=pk)
#     if request.method == 'POST':
#         customer.delete()
#         return redirect('customerRecords')
#     context={'customer':customer}
#     return render(request, 'customers/deleteCustomer.html', context)

# #generate Report
# @login_required(login_url='login')   
# def Customer_report(request):
#     response= HttpResponse(content_type='text/csv')
#     response['content-Disposition']= 'attachment; filename= CustomerReport.csv'
#     #create a csv Writer
#     writer= csv.writer(response)
#     #Designate the model
#     customers = Customers.objects.all()
#     #add column heading to the csv file 
#     writer.writerow(['First Name', 'Last Name', 'Address', 'Phone'])
#     #Loop Through the customers object and output
#     for customer in customers:
#         writer.writerow([customer.firstName, customer.lastName, customer.address, customer.contact])
#     return response