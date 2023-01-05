from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=300)
    customer_phoneno = models.CharField(max_length=20)
