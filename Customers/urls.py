from django.urls import path
from Customers import views

urlpatterns = [
    path('registerCustomer/', views.registerCustomer, name="registerCustomer"),
    path('customerRecords/', views.customerRecords, name="customerRecords"),
    path('customer_details/<str:pk>/', views.customer_detailView, name="customer_details"),
    path('UpdateCustomer/<str:pk>/', views.UpdateCustomer, name = "UpdateCustomer"),
    path('deleteCustomer/<str:pk>/',views.deleteCustomer, name="deleteCustomer"),
    path('customer_report/', views.Customer_report, name="customer_report")
]