from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images')
    description= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)
    status=models.BooleanField(default=False)


class Cart(models.Model):
    fk_user = models.ForeignKey(User,on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    sub_total=models.DecimalField(max_digits=10, decimal_places=2)


    