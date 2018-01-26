from django.db import models

# Create your models here.
class Product(models.Model):

    #id = models.CharField(max_length=140, primary_key=True)
    product_name = models.CharField(max_length=140)
    product_description = models.CharField(max_length=1000)
    product_price = models.CharField(max_length=10)
    is_syndicated = models.BooleanField(default=False)
