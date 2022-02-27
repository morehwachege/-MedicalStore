from django.db import models
from django.utils import timezone

# Create your models here
#Choice field for medicine category
categoryChoice = (
    ('painkillers', 'painkillers'),
    ('antibiotics', 'antibiotics'),
    ('contraceptives', 'contarceptives'),
)

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)

   

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    MedicineName = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    medicineId = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.IntegerField(default=0, null=True)
    issueQuantity =models.IntegerField(null=True, default=0)
    reorderLevel = models.IntegerField(null=True)
    issueTo = models.CharField(max_length=50, null=True)
    receivedBy = models.CharField(max_length=50, null=True)
    receiveQuantity = models.IntegerField(null=True, default=0)
    added_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdated= models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.MedicineName
 

    class MedicineDetails(models.Model):
        id = models.AutoField(primary_key=True)
        description = models.CharField(max_length=255)
        added_on = models.DateTimeField(auto_now_add=True)

      
class Pharmacist(models.Model):
    id = models.AutoField(primary_key=True)
    pharmacistName = models.CharField(max_length =30)
    joining_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField()

    def __str__(self):
     return self.name
        

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255,)
    lastName = models.CharField(max_length=255,)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName