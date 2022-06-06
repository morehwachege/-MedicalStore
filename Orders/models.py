# from django.db import models
# from PharmacyManagementSystem.models import Medicine, Customers

# Create your models here.
# class Orders(models.Model):
#     customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customers")
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="medicine")
#     quantity = models.PositiveBigIntegerField()
#     price =  models.FloatField()
#     total_price = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)
#     date_updated= models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.customer.firstName
    
#     def save(self, *args, **kwargs):
#         self.total_price = self.quantity*self.price
#         super().save(**args, **kwargs)

