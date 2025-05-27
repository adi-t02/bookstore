
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from bookstore_app.forms import LoginRegister, CustomerRegister
from bookstore_app.models import Customer, Cart, Products, Sold, Review

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

@login_required(login_url='login')
def customer_page(request):
    return render(request,"customer/customer_page.html")


@login_required(login_url='login')
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


@login_required(login_url='login')
def customer_list(request):
    data = Customer.objects.all
    return render(request,'customer/customer_view.html',{'data':data})

@login_required(login_url='login')
def customer_delete(request,id):
    data =Customer.objects.get(id=id)
    data.delete()
    return redirect('customer_list')

@login_required(login_url='login')
def customer_profile(request):
    profile_id = request.user
    data = Customer.objects.get(user= profile_id)
    return render(request, 'customer/profile.html', {'user': data})

@login_required(login_url='login')
def customer_update(request,id):
    data = Customer.objects.get(id=id)
    customer_form = CustomerRegister(instance=data)
    if request.method == 'POST':
        form1 = CustomerRegister(request.POST, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,"customer/update.html",{'form':customer_form})

@login_required(login_url='login')
def cart_add(request,id):
    if not request.user.is_authenticated:
        return redirect("login")

    else:
        user_id = request.user
        buyer_id = Customer.objects.get(user = user_id)
        product_id = Products.objects.get(id = id)
        if Cart.objects.filter(buyer=buyer_id, product=product_id).exists():
            messages.info(request, '')
        else:
            obj = Cart()
            obj.buyer = buyer_id
            obj.product  = product_id
            obj.quantity = 1
            obj.save()
            # messages.info(request, "")
    return redirect('/')

# Cart.objects.create(customer = x,pro = y )

@login_required(login_url='login')
def cart_view(request):
    user_id = request.user
    buyer_id = Customer.objects.get(user = user_id)
    items = Cart.objects.filter(buyer = buyer_id)
    total = 0
    for item in items:
        total = int(item.product.price)+total

    context = {
        'total':total,
        'items':items
    }
    return render(request,'customer/cart.html',context)


@login_required(login_url='login')
def cart_delete(request,id):
    item = Cart.objects.get(id = id)
    item.delete()
    return redirect('cart_view')


@login_required(login_url='login')
def products_page(request,id):
    if not request.user.is_authenticated:
        return redirect("login")
    data = Products.objects.get(id = id)
    reviews = Review.objects.filter(product__id = id)
    stock = int(data.stock)
    if request.method == 'POST':
        user_id = request.user
        buyer_id = Customer.objects.get(user=user_id)
        count = request.POST.get("quantity")
        # print(type(count))
        obj = Sold()
        obj.buyer = buyer_id
        obj.quantity = count
        obj.product = data
        if stock >= count:
            data.stock = stock - count
            data.save()
            obj.save()
            return redirect('/')


        else:
            messages.info(request,"not in stock")

    context ={
        'item': data,
        'reviews':reviews

    }

    return render(request,'customer/products.html',context)



@login_required(login_url='login')
def order_list(request):
    user_id = request.user
    customer_id = Customer.objects.get(user=user_id)
    items = Sold.objects.filter(buyer = customer_id)
    return render(request,'customer/order_list.html',{'items':items})


@login_required(login_url='login')
def buy_now(request,id):
    data = Cart.objects.get(id=id)
    stock = int(data.product.stock)
    if request.method == 'POST':
        user_id = request.user
        buyer_id = Customer.objects.get(user=user_id)
        count = int(request.POST.get("quantity"))
        print(type(count))
        obj = Sold()
        obj.buyer = buyer_id
        obj.quantity = count
        obj.product = data.product
        if stock >= count:
            data.product.stock = stock - count
            data.save()
            obj.save()
            data.delete()
            return redirect('cart_view')


        else:
            messages.info(request, "not in stock")

    return render(request, 'customer/buynow.html', {'item': data})


@login_required(login_url='login')
def review_add(request,id):
    product_id = Sold.objects.get(id = id)
    if request.method == 'POST':
        user_id = request.user
        buyer_id = Customer.objects.get(user=user_id)
        review = request.POST.get("review")
        obj = Review()
        obj.buyer = buyer_id
        obj.product = product_id.product
        obj.review = review
        obj.save()
        return redirect('order_list')
    return render(request,'customer/review.html')


@login_required(login_url='login')
def print_invoice(request,id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, height - 100, "Invoice")

    user_id = request.user
    username = Customer.objects.get(user = user_id)
    item = Sold.objects.get(id = id)
    total = int(item.product.price)*item.quantity

    y = height - 140
    p.drawString(100, y, f"Customer: {username.name}")
    y -= 40


    p.setFont("Helvetica", 12)

    p.drawString(100, y, f"Item :{item.product.name}")
    y -= 20
    p.drawString(100, y, f"quantity :{item.quantity}")
    y -= 20
    p.drawString(100, y, f"Price :${item.product.price}")
    y -= 20


    # p.drawString(100, y, f"{item.product.name}")
    # p.drawString(300, y, f"{item.product.stock}")
    # p.drawString(450, y, f"${item.product.price}")
    # y -= 20

    # Total
    y -= 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y, "Total")
    p.drawString(300, y, f"${total}")

    # Finalize PDF
    p.showPage()
    p.save()
    return response