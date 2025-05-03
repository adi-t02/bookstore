from django.shortcuts import render, redirect

from bookstore_app.forms import SellerRegister, LoginRegister
from bookstore_app.models import Seller


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
    return render(request,'admin/seller_view.html',{'data':data})
