
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app import views


urlpatterns = [
    path('', include('Users.urls')),

    path('medList/',views.medList, name="medList"),
    path('addMedicine/',views.addMedicine, name="addMedicine"),
    path('MedicineUpdate/<str:pk>/', views.MedicineUpdate, name = "MedicineUpdate"),
    path('medicineDetail/<str:pk>/', views.medicineDetail, name="medicineDeatil"),
    path('IssueMedicine/<str:pk>/', views.IssueMedicine, name="IssueMedicine"),
    path('ReceiveMedicine/<str:pk>/', views.ReceiveMedicine, name="ReceiveMedicine"),
    path('medReorderLevel/<str:pk>', views.medReorderLevel, name="medReorderLevel"),
    path('deleteMedicine/<str:pk>/', views.deleteMedicine, name="deleteMedicine"),

    path('addPharmacist/', views.addPharmacist, name="addPharmacist"),
    path('pharmacistRecord/', views.pharmacistRecord, name="pharmacistRecord"),
    path('medicineReport/', views.Medicine_Report, name="medicineReport"),
    path('admin/', admin.site.urls),
    #path('accounts/', include('registration.backends.default.urls')),

    path('registerCustomer/', views.registerCustomer, name="registerCustomer"),
    path('customerRecords/', views.customerRecords, name="customerRecords"),
    path('customer_details/<str:pk>/', views.customer_detailView, name="customer_details"),
    path('UpdateCustomer/<str:pk>/', views.UpdateCustomer, name = "UpdateCustomer"),
    path('deleteCustomer/<str:pk>/',views.deleteCustomer, name="deleteCustomer"),
    path('customer_report/', views.Customer_report, name="customer_report"),

    path('new_order/', views.create_order, name="new_order"),
    path('orders/', views.orders_view, name="orders"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('print_receipt/<str:pk>/', views.print_receipt, name="print_receipt"),
    path('order_report/', views.order_report, name="order_report"),
]
