from django.db import models
from seller.models import Product
from common.models import Customer

# Create your models here.
class Cart(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(max_length=50,default=1) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, default='')
    