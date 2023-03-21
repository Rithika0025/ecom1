from django.shortcuts import render,redirect

from common.models import Customer
from seller.models import Product
from customer.models import Cart
from .decorator import auth_customer
# Create your views here.
def customer_master(request):
    return render(request,'customer_temp/master2.html')

@auth_customer
def customer_home(request):
    return render(request,'customer_temp/home2.html')

def customer_product_details(request):
    customer_products = Product.objects.all()
    return render(request,'customer_temp/pro_details.html' , {'productlist' : customer_products})

def customer_myorder(request):
    return render(request,'customer_temp/myorder.html')

@auth_customer
def customer_profile(request):
    
    #if session_id in requst.session
        #variable=Class.objects.get (oru variable lek aa session il ulla aalde details)
     
    currentuser = Customer.objects.get(id = request.session['customer'])
    return render(request,'customer_temp/profile.html',{'user_details' : currentuser})
                        #dictionary aayit kodukum oru new variable lek :aa login cheytha aalde details html  il veran,ee variable aan html il page il call aakne
   
    

def change_password(request):
    success_msg = ''
    error_msg = ''
    if request.method == 'POST':
        old_pass = request.POST ['old_password'] 
        new_pass = request.POST ['new_password']
        confirm_pass = request.POST ['confirm_password']
       
        customer = Customer.objects.get(id = request.session['customer'])
       
        if new_pass == confirm_pass:
           if len(new_pass) >=8:
                  if customer.customer_password  == old_pass:
                    customer.customer_password = new_pass
                    customer.save()
                    success_msg = 'password changed'
                  else:
                      error_msg = 'incorrect password'
                

           else:
               error_msg = 'password should be minimum 8 characters'
        else:
           error_msg = 'Password does not match'
           

    return render(request,'customer_temp/change_password.html',{'success_msg':success_msg,'error_msg':error_msg})

def logout(request):
    del request.session['customer']
    # return render (request,'common/custlogin1.html')
    return redirect('common:custlogin1')

def view_products(request,product_id):
    viewpro = Product.objects.get(id=product_id)
    
    return render(request,'customer_temp/view_pro.html',{'view_product':viewpro})

def add_to_cart(request,product_id) :
    cart_object = Cart.objects.filter(customer_id = request.session ['customer'],products_id = product_id).exists()
    if not cart_object: 
        cart = Cart.objects.create(
            customer_id = request.session['customer'],
            products_id = product_id,    
            )
    else:
        cart = Cart.objects.get(customer_id = request.session ['customer'],products_id = product_id)    
        cart.quantity = cart.quantity + 1
        cart.save()
      
        
    return redirect ('customer:productdetail')

def customer_cart(request):
    cart = Cart.objects.filter(customer_id = request.session ['customer'])
    return render(request,'customer_temp/cart.html',{'cart_product': cart})

def change_quantity(request):
    error_msg = ''
    # success_msg = ''
    quantity = int(request.POST['quantity'])
    product_id = int(request.POST['product_id'])
    current_stock = Product.objects.get(id = product_id).current_stock
    if quantity > current_stock :
        error_msg = 'Out of stock'
    else:
        error_msg = 'In stock'
    return JsonResponse({'error_msg': error_msg})

    
