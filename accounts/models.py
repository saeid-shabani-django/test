from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)

