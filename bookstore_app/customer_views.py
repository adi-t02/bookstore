from django.shortcuts import redirect, render

from bookstore_app.forms import LoginRegister, CustomerRegister

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



