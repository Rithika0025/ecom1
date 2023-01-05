from django.shortcuts import render

from common.models import Customer

# Create your views here.
def common_master(request):
    return render(request,'common/master1.html')
def common_home(request):
    return render(request,'common/home1.html')
def common_custlogin(request):
    return render(request,'common/custlogin1.html')
def common_custreg(request):
    if request.method == 'POST':
        cust_name = request.POST ['c_name']
        cust_email = request.POST ['c_email']
        cust_pass = request.POST ['c_password']
        cust_address = request.POST ['c_address']
        cust_phone = request.POST ['c_phone']
        
        # QUICK FIX KODUKANM
        customer1 = Customer(
            customer_name = cust_name,
            customer_email = cust_email,
            customer_password = cust_pass,
            customer_address = cust_address,
            customer_phoneno = cust_phone
            # models il ullath = views il ullath
        )
        customer1.save()
    return render(request,'common/custreg1.html')
def common_sellogin(request):
    return render(request,'common/sellogin1.html')
def common_selreg(request):
    return render(request,'common/selreg1.html')
