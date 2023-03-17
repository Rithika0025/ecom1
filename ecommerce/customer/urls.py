from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
    path('master2',views.customer_master,name='master2'),
    path('home2',views.customer_home,name='home2'),
    path('productdetail',views.customer_product_details,name='productdetail'),
    path('myorder',views.customer_myorder, name='myorder'),
    path('profile',views.customer_profile,name='profile'),
    path('change_password',views.change_password,name='change_password'),
    path('logout',views.logout,name='logout'),
    path('view_pro/<int:product_id>',views.view_products,name='viewpro'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='addtocart'),
    path('cart',views.customer_cart,name='cart'),
]