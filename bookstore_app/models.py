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
    cover = models.ImageField(upload_to='bookcovers/')
    category = models.CharField(max_length=20, choices=STATUS_CHOICES, default='others')
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.CharField(max_length=10)

class Cart(models.Model):
    product =  models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

class Sold(models.Model):
    product =  models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()


class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)