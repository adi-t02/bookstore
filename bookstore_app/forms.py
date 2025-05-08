from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Login_view, Customer, Seller, Products


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username', 'password1', 'password2')



class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'address')


class SellerRegister(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'email', 'phone', 'address')



class ProductsForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name','category','description','stock','price')