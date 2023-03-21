from django.http import HttpResponseRedirect 
from django.shortcuts import redirect

def auth_seller(func) :
    def wrapper (request, *args, **kwargs):
        if 'seller' not in request.session:
                return redirect('common:sellogin1')
        else:
                return func (request, *args, **kwargs)
    return wrapper
