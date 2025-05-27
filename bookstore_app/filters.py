import django_filters
from django import forms
from django_filters import CharFilter

from bookstore_app.models import Products


class ProductsFilters(django_filters.FilterSet):
    name = CharFilter(field_name='name',label='',lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search','class':'form-control'}))


    class Meta:
        model = Products
        fields = ('name',)



# class BookFilters(django_filters.FilterSet):
#     name = CharFilter(field_name='name',label='',lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search','class':'form-control'}))
#
#
#     class Meta:
#         model = Products
#         fields = ('name',)