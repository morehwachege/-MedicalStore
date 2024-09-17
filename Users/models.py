from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    joining_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-added_on']

    def __str__(self):
        return self.username
