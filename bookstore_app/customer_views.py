from django.shortcuts import redirect, render

from bookstore_app.forms import LoginRegister, CustomerRegister
from bookstore_app.models import Customer


def customer_page(request):
    return render(request,"customer/customer_page.html")


def customer_add(request):
    login_form = LoginRegister()
    customer_form = CustomerRegister()

    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        customer_form = CustomerRegister(request.POST)

        if login_form.is_valid() and customer_form.is_valid():
            cust = login_form.save(commit=False)
            cust.is_customer = True
            cust.save()

            user1 = customer_form.save(commit=False)
            user1.user = cust
            user1.save()
            return redirect('/')
    return render(request,"customer/registor.html",{'login_form':login_form,'customer_form':customer_form})



def customer_list(request):
    data = Customer.objects.all
    return render(request,'customer/customer_view.html',{'data':data})


def customer_delete(request,id):
    data =Customer.objects.get(id=id)
    data.delete()
    return redirect('customer_list')


def customer_profile(request):
    profile_id = request.user
    data = Customer.objects.get(user= profile_id)
    return render(request, 'customer/profile.html', {'user': data})


def customer_update(request,id):
    data = Customer.objects.get(id=id)
    customer_form = CustomerRegister(instance=data)
    if request.method == 'POST':
        form1 = CustomerRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,"customer/update.html",{'form':customer_form})
