from django.db import models
from common.models import Seller

# Create your models here.
class Product(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_no = models.CharField(max_length=18)
    description = models.CharField(max_length=200)
    price = models.FloatField(max_length=60)
    current_stock = models.CharField(max_length=50)
    product_pic = models.ImageField(upload_to='product/')