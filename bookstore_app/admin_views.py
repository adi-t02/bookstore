from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bookstore_app.models import Products, Sold

@login_required(login_url='login')
def admin_page(request):
    return render(request,"admin/admin_base.html")

@login_required(login_url='login')
def product_view(request):
    data = Products.objects.all
    return render(request, 'admin/products_view.html', {'data': data})

@login_required(login_url='login')
def sold_page(request):
    data = Sold.objects.all
    return render(request,'admin/sold_page.html',{'data':data})
