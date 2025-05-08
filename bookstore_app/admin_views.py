from django.shortcuts import render

from bookstore_app.models import Products


def admin_page(request):
    return render(request,"admin/admin_base.html")


def product_view(request):
    data = Products.objects.all
    return render(request, 'admin/products_view.html', {'data': data})