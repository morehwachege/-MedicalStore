from django.db import models
from PharmacyManagementSystem.models import Medicine

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=255,)
    lastName = models.CharField(max_length=255,)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    medicine = models.ForeignKey(Medicine, blank=True, default=1, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    # height = models.PositiveIntegerField(null=True)
    # weight = models.PositiveIntegerField(null=True)   
    

    def __str__(self):
        return self.firstName
    
    

   

