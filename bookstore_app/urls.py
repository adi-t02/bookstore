from django.urls import path, include

from bookstore_app import views, customer_views, seller_views, admin_views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name="login"),
    path('logout',views.logout_view,name="logout"),

    #customer
    path('customer_add',customer_views.customer_add,name="customer_add"),
    path('customer_page',customer_views.customer_page,name="customer_page"),
    #seller
    path('seller_add',seller_views.seller_add,name="seller_add"),
    path('seller_page',seller_views.seller_page,name="seller_page"),
    path('seller_list',seller_views.seller_list,name="seller_list"),
    #admin
    path('admin_page',admin_views.admin_page,name="admin_page"),
]
