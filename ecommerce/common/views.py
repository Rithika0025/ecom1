import random
from django.shortcuts import render,redirect

from common.models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def common_master(request):
    return render(request,'common/master1.html')

def common_home(request):
    return render(request,'common/home1.html')

def common_custlogin(request):
    msg = ""
    if request.method == 'POST':
        cust_email1 = request.POST['c_email1'] #input variable login ullath
        cust_pass1 = request.POST['c_pass1']
        
        try : 
            customer = Customer.objects.get(
                customer_email = cust_email1,  
                customer_password = cust_pass1
                )          
            request.session['customer'] = customer.id
            return redirect ('customer:productdetail')
        except :
            msg = 'invalid password or username'
            
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
        
        return redirect ('customer:home2')
    return render(request,'common/custreg1.html')

def common_sellogin(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['s_username'] #input variable login ullath
        password = request.POST['s_password']
        print(password)
        # try : 
        seller= Seller.objects.get(seller_username=username,seller_password=password)          
        request.session['seller'] = seller.id
        return redirect ('seller:home3')
        # except :
        #     msg = 'invalid password or username'
    return render(request,'common/sellogin1.html',{'msg':msg})

def common_selreg(request):
    if request.method == 'POST':
        seller_name = request.POST['sel_name']
        seller_phone = request.POST['sel_phone']
        seller_address = request.POST['sel_address']
        seller_holder_name = request.POST['holder_name']
        seller_ifsc = request.POST['sel_ifsc']
        seller_branch = request.POST['sel_branch']
        seller_accno = request.POST['sel_accno']
        seller_email = request.POST['sel_email']
        photo = request.FILES['pic']
        seller_username = random.randint(1111,9999)
        seller_password = 'sel-'+ seller_name.lower() + str(seller_username)
        message = 'hai your username is' + str(seller_username)+'and temporary password is ' + seller_password 
        
        newseller = Seller(
            seller_name = seller_name,
            phone = seller_phone,
            address = seller_address,
            account_holder_name = seller_holder_name,
            ifsc_code = seller_ifsc,
            bank_branch = seller_branch,
            account_number = seller_accno,
            email = seller_email,
            seller_username = seller_username,
            seller_password = seller_password,
            seller_pic = photo
        )
        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email],
            fail_silently=False
        )
        newseller.save()
    return render(request,'common/selreg1.html')
