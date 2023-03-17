from django.http import HttpResponseRedirect 
from django.shortcuts import redirect

# divide func divide aakmbm velya number/cheriya number veran ulla decorator
def divide_dec (func):
    def wrapper(a,b):
        if b > a:
            a,b = b,a
        return func(a,b)
    return wrapper
    
    
@divide_dec  
def divide(a,b):
    result = a/b
    print (result)
    
divide(2,10)



# oral login cheytha mathrm avrde detail vanna madhi athina ee decorators.ith views @ use cheyth func call cheyya
def auth_customer(func) :
    def wrapper (request, *args, **kwargs):
        if 'customer' not in request.session:
                return redirect('common:custlogin1')
        else:
                return func (request, *args, **kwargs)
    return wrapper
