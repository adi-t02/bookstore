from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bookstore_app.filters import ProductsFilters
from bookstore_app.forms import SellerRegister, LoginRegister, ProductsForms
from bookstore_app.models import Seller, Products, Sold

@login_required(login_url='login')
def seller_page(request):
    return render(request,"seller/seller_page.html")


@login_required(login_url='login')
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


@login_required(login_url='login')
def seller_list(request):
    data = Seller.objects.all
    return render(request,'seller/seller_view.html',{'data':data})


@login_required(login_url='login')
def seller_delete(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('seller_list')


@login_required(login_url='login')
def seller_profile(request):
    profile_id = request.user
    data = Seller.objects.get(user=profile_id)
    return render(request, 'seller/profile.html', {'user': data})


@login_required(login_url='login')
def seller_update(request,id):
    data = Seller.objects.get(id=id)
    form = SellerRegister(instance=data)
    if request.method == 'POST':
        form1 = SellerRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('seller_page')
    return render(request,"seller/update.html",{'form':form})


@login_required(login_url='login')
def product_add(request):
    user_data = request.user
    seller_data = Seller.objects.get(user = user_data)
    form = ProductsForms()
    if request.method == 'POST':
        form = ProductsForms(request.POST,request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.seller = seller_data
            form1.save()
            return redirect('seller_page')
    return render(request,"seller/add_products.html",{"form":form})


@login_required(login_url='login')
def product_view(request):
    user_id = request.user
    seller_id = Seller.objects.get(user = user_id)
    data = Products.objects.filter(seller = seller_id.id)
    filter_products = ProductsFilters(request.GET,queryset=data)
    data1 = filter_products.qs
    context = {
        'data':data1,
        'filter_products':filter_products,
    }
    return render(request, 'seller/product_view.html', context)


@login_required(login_url='login')
def sold_list(request):
    user_id = request.user
    seller_id = Seller.objects.get(user=user_id)

    data = Sold.objects.filter(product__seller = seller_id)
    print(data)
    return render(request, 'seller/sold_view.html',{'data':data} )
