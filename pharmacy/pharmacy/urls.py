"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from PharmacyManagementSystem import views


urlpatterns = [
    path('', views.index, name="index"),
    path('medList/',views.medList, name="medList"),
    path('addMedicine/',views.addMedicine, name="addMedicine"),
    path('MedicineUpdate/<str:pk>/', views.MedicineUpdate, name = "MedicineUpdate"),
    path('medicineDetail/<str:pk>/', views.medicineDetail, name="medicineDeatil"),
    path('IssueMedicine/<str:pk>/', views.IssueMedicine, name="IssueMedicine"),
    path('ReceiveMedicine/<str:pk>/', views.ReceiveMedicine, name="ReceiveMedicine"),
    path('medReorderLevel/<str:pk>', views.medReorderLevel, name="medReorderLevel"),
    path('deleteMedicine/<str:pk>/', views.deleteMedicine, name="deleteMedicine"),
    path('registerCustomer/', views.registerCustomer, name="registerCustomer"),
    path('customerRecords/', views.customerRecords, name="customerRecords"),
    path('UpdateCustomer/<str:pk>/', views.UpdateCustomer, name = "UpdateCustomer"),
    path('deleteCustomer/<str:pk>/',views.deleteCustomer, name="deleteCustomer"),
    path('addPharmacist/', views.addPharmacist, name="addPharmacist"),
    path('pharmacistRecord/', views.pharmacistRecord, name="pharmacistRecord"),
    
    path('admin/', admin.site.urls),
    #path('accounts/', include('registration.backends.default.urls')),
]
