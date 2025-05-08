from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from bookstore_app import views, customer_views, seller_views, admin_views

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
    #seller
    path('seller_add',seller_views.seller_add,name="seller_add"),
    path('seller_page',seller_views.seller_page,name="seller_page"),
    path('seller_list',seller_views.seller_list,name="seller_list"),
    path('seller_delete/<int:id>',seller_views.seller_delete,name="seller_delete"),
    path('seller_profile',seller_views.seller_profile,name="seller_profile"),
    path('seller_update/<int:id>',seller_views.seller_update,name="seller_update"),
    path('product_add',seller_views.product_add,name="product_add"),
    path('product_view',seller_views.product_view,name="product_view"),
    #admin
    path('admin_page',admin_views.admin_page,name="admin_page"),
    path("products_admin",admin_views.product_view,name="products_admin")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)