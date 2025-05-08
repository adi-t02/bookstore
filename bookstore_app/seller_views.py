from django.shortcuts import render, redirect

from bookstore_app.forms import SellerRegister, LoginRegister, ProductsForms
from bookstore_app.models import Seller, Products


def seller_page(request):
    return render(request,"seller/seller_page.html")


def seller_add(request):
    login_form = LoginRegister()
    seller_form = SellerRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        seller_form = SellerRegister(request.POST)

        if login_form.is_valid() and seller_form.is_valid():
            seller = login_form.save(commit=False)
            seller.is_seller = True
            seller.save()

            user1 = seller_form.save(commit=False)
            user1.user = seller
            user1.save()
            return redirect('seller_page')
    return render(request,"customer/registor.html",{'login_form':login_form,'customer_form':seller_form})


def seller_list(request):
    data = Seller.objects.all
    return render(request,'seller/seller_view.html',{'data':data})


def seller_delete(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('seller_list')


def seller_profile(request,id):
    data = Seller.objects.get(user_id=id)
    return render(request, 'seller/profile.html', {'user': data})


def seller_update(request,id):
    data = Seller.objects.get(id=id)
    form = SellerRegister(instance=data)
    if request.method == 'POST':
        form1 = SellerRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('seller_page')
    return render(request,"seller/update.html",{'form':form})


def product_add(request):
    user_data = request.user
    seller_data = Seller.objects.get(user = user_data)
    form = ProductsForms()
    if request.method == 'POST':
        form = ProductsForms(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.seller = seller_data
            form1.save()
            return redirect('seller_page')
    return render(request,"seller/add_products.html",{"form":form})


def product_view(request):
    user_id = request.user
    seller_id = Seller.objects.get(user = user_id)
    data = Products.objects.filter(seller = seller_id.id)
    return render(request, 'seller/product_view.html', {'data': data})