from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    medicine_id = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reorder_level = models.PositiveIntegerField(null=True, blank=True)
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def update_stock(self, quantity):
        """Update stock quantity and handle reorder level alert."""
        self.quantity -= quantity
        if self.quantity < 0:
            self.quantity = 0  # Prevent negative stock
        self.save()

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name}"

    def save(self, *args, **kwargs):
        """Calculate total amount and update medicine stock when saving the order."""
        if self.pk is None:  # Only calculate total amount for new orders
            self.total_amount = sum(item.total_price for item in self.orderitem_set.all())
        super().save(*args, **kwargs)  # Save the order first
        for item in self.orderitem_set.all():
            item.medicine.update_stock(item.quantity)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """Calculate total price before saving."""
        self.total_price = self.quantity * self.price
        super().save(*args, **kwargs)
