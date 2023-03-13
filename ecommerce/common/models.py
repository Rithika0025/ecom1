from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=300)
    customer_phoneno = models.CharField(max_length=20)

class Seller(models.Model):
    seller_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=18)
    address=models.CharField(max_length=200)
    account_holder_name=models.CharField(max_length=60)
    ifsc_code=models.CharField(max_length=50)
    bank_branch=models.CharField(max_length=100)
    account_number=models.CharField(max_length=50)
    seller_username = models.CharField(max_length=30)
    seller_password = models.CharField(max_length=50)
    seller_pic = models.ImageField(upload_to='seller/')