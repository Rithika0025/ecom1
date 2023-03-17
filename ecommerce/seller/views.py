import json
from django.http import JsonResponse
from django.shortcuts import render,redirect

from seller.models import Product

# Create your views here.
def seller_master(request):
    return render(request,'seller/master3.html')

def seller_addpro(request):
    if request.method == 'POST':
        category = request.POST ['p_category']
        pro_name = request.POST ['p_name']
        pro_no = request.POST ['p_number']
        description = request.POST ['p_description']
        price = request.POST ['p_price']
        stock = request.POST ['p_stock']
        photo = request.FILES['p_image']
        #namal kodukkunna variable = requst .post ['form il ullath']
        
        
        # QUICK FIX KODUKANM
        #ith object aan =Classname
        #models = new varaible ivde koduthe
        newproduct = Product(
            category = category,
            product_name =pro_name,
            product_no = pro_no,
            description = description,
            price = price,
            current_stock = stock,
            product_pic = photo,
            seller_id_id = request.session['seller']
        )
        newproduct.save()
    return render(request,'seller/add_product.html')

def seller_home(request):
    return render(request,'seller/home3.html')

def seller_profile(request):
    return render(request,'seller/profile.html')

def seller_vieworder(request):
    return render(request,'seller/view_order.html')

def seller_viewpro(request):
    seller_product = Product.objects.filter(
        seller_id = request.session['seller']  
    )
    return render(request,'seller/view_product.html',{'products' : seller_product })

def seller_viewpayment(request):
    return render(request,'seller/view_payment.html')

def logout(request):
    del request.session['seller']
    # return render (request,'common/custlogin1.html')
    return redirect('common:sellogin1')

def del_product(request,p_id):
    delete_product = Product.objects.get(id = p_id)
    delete_product.delete()
    return redirect('seller:viewpro')

def seller_updatestock(request):
    return render(request,'seller/update_stock.html')

def get_product(request):
    category = request.POST['category_key']
    product = Product.objects.filter(seller_id= request.session ['seller'],category = category )
                                                                            #models=ivde ulla category
    data = [{'product_name':pro.product_name,'id':pro.id}
            for pro in product]
    return JsonResponse({'data':data})

