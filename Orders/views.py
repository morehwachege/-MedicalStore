# from django.shortcuts import render, redirect
# from Orders.models import Order
# from Orders.forms import OrderCreateForm, OrderUpdateForm
# # Create your views here.

# @login_required(login_url='login')   
# def create_order(request):
#     form = OrderCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('orders')
#     context ={
#             "form": form,
#             "title": "Create New Order"
#         }
#     return render(request, "orders/create_order.html", context)

# # @login_required(login_url='login')   
# def orders_view(request):
#     title = 'Sales'
#     orders = Order.objects.all()
#     context ={
#         "title": title,
#         "customers":orders,
#     }
#     return render(request, "orders/orders.html", context)

# # #update customer record
# # @login_required(login_url='login')   
# def update_order(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderUpdateForm(instance = order)
#     if request.method == 'POST':
#         form = OrderUpdateForm(request.POST, instance = order)
#         if form.is_valid():
#             form.save()
#         return redirect('orders')
#     context ={
#         "form":form,
#         "title": "Update Item"
#     }
#     return render(request, 'orders/create_order.html', context)

# # #Delete Record
# # @login_required(login_url='login')   
# def delete_order(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('customerRecords')
#     context={'order':order}
#     return render(request, 'orders/delete_order.html', context)

# # #generate Report
# # @login_required(login_url='login')   
# # def Customer_report(request):
# #     response= HttpResponse(content_type='text/csv')
# #     response['content-Disposition']= 'attachment; filename= CustomerReport.csv'
# #     #create a csv Writer
# #     writer= csv.writer(response)
# #     #Designate the model
# #     customers = Customers.objects.all()
# #     #add column heading to the csv file 
# #     writer.writerow(['First Name', 'Last Name', 'Address', 'Phone'])
# #     #Loop Through the customers object and output
# #     for customer in customers:
# #         writer.writerow([customer.firstName, customer.lastName, customer.address, customer.contact])
# #     return response