from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from bookstore_app import views, customer_views, seller_views, admin_views
from bookstore_app.customer_views import products_page

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name="login"),
    path('logout',views.logout_view,name="logout"),

    #customer
    path('customer_add',customer_views.customer_add,name="customer_add"),
    path('customer_page',customer_views.customer_page,name="customer_page"),
    path('customer_list',customer_views.customer_list,name="customer_list"),
    path('customer_delete/<int:id>',customer_views.customer_delete,name="customer_delete"),
    path('customer_profile',customer_views.customer_profile,name="customer_profile"),
    path('customer_update/<int:id>',customer_views.customer_update,name="customer_update"),
    path('cart_add/<int:id>',customer_views.cart_add,name="cart_add"),
    path('cart_view',customer_views.cart_view,name="cart_view"),
    path('cart_delete/<int:id>',customer_views.cart_delete,name="cart_delete"),
    path('products_page/<int:id>',customer_views.products_page,name="products_page"),
    path('order_list',customer_views.order_list,name="order_list"),
    path('buy_now/<int:id>',customer_views.buy_now,name="buy_now"),
    path('review_add/<int:id>',customer_views.review_add,name="review_add"),
    path('print_invoice/<int:id>',customer_views.print_invoice,name="print_invoice"),
    #seller
    path('seller_add',seller_views.seller_add,name="seller_add"),
    path('seller_page',seller_views.seller_page,name="seller_page"),
    path('seller_list',seller_views.seller_list,name="seller_list"),
    path('seller_delete/<int:id>',seller_views.seller_delete,name="seller_delete"),
    path('seller_profile',seller_views.seller_profile,name="seller_profile"),
    path('seller_update/<int:id>',seller_views.seller_update,name="seller_update"),
    path('product_add',seller_views.product_add,name="product_add"),
    path('product_view',seller_views.product_view,name="product_view"),
    path('sold_list',seller_views.sold_list,name="sold_list"),
    #admin
    path('admin_page',admin_views.admin_page,name="admin_page"),
    path("products_admin",admin_views.product_view,name="products_admin"),
    path("sold_page",admin_views.sold_page,name="sold_page")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)