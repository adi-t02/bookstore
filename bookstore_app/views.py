from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from bookstore_app.filters import ProductsFilters
from bookstore_app.models import Products, Customer, Cart


# Create your views here.
def home(request):
    books= Products.objects.all()
    filter_books = ProductsFilters(request.GET, queryset=books)
    books = filter_books.qs

    context={
        'bookss':books,
        'filter_books':filter_books
    }
    return render(request,"home/home.html",context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('user1')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_customer:
                return redirect('home')
            elif user.is_seller:
                return redirect('seller_page')
        else:
            messages.info(request,"invalid username or password")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('home')