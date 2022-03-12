from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=255,)
    lastName = models.CharField(max_length=255,)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName