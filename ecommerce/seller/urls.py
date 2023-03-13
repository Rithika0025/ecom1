from django.urls import path
from . import views
app_name = 'seller'
urlpatterns = [
    path('master3',views.seller_master,name='master3'),
    path('home3',views.seller_home,name='home3'),
    path('viewpro',views.seller_viewpro,name='viewpro'),
    path('addpro',views.seller_addpro,name='addpro'),
    path('profile',views.seller_profile,name='profile'),
    path('viewpayment',views.seller_viewpayment,name='viewpayment'),
    path('vieworder',views.seller_vieworder,name='vieworder'),
    path('logout',views.logout,name='logout'),
]