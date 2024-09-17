from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_stock(sender, instance, **kwargs):
    for item in instance.orderitem_set.all():
        medicine = item.medicine
        medicine.stock -= item.quantity
        medicine.save()
