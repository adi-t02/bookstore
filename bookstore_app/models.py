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


class Products(models.Model):
    STATUS_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('History', 'History'),
        ('Autobiography', 'Autobiography'),
        ('Science fiction', 'Science fiction'),
        ('Adventure fiction', 'Adventure fiction'),
        ('Biography', 'Biography'),
        ('Poetry', 'Poetry'),
        ('Romance novel', 'Romance novel'),
        ('others','others')
    ]
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=STATUS_CHOICES, default='others')
    description = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    stock = models.CharField(max_length=5)
    price = models.CharField(max_length=10)

