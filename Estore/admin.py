from django.contrib import admin
from .models import ProductModel
# Register your models here.
from django.utils.timesince import timesince

class ProductAdmin(admin.ModelAdmin):
    
    list_display=['title','productImage','price','created']
admin.site.register(ProductModel,ProductAdmin)