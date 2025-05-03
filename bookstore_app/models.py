from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class Seller(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
