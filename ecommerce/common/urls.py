from django.urls import path
from . import views
app_name = 'common'
urlpatterns = [
    path('master1',views.common_master,name='master1'),
    path('home1',views.common_home,name='home1'),
    path('custlogin1',views.common_custlogin,name='custlogin1'),
    path('sellogin1',views.common_sellogin,name='sellogin1'),
    path('custreg1',views.common_custreg,name='custreg1'),
    path('selreg1',views.common_selreg,name='selreg1'),
    path('emailexist',views.email_exists,name='email_exists'),
]
