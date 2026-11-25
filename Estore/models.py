from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title=models.CharField(max_length=200,unique=True)
    content=models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)