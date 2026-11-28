from django.contrib import admin
from .models import ProductModel,ArticleModel
# Register your models here.
from django.utils.timesince import timesince

class ProductAdmin(admin.ModelAdmin):
    
    list_display=['title','productImage','price','created']
admin.site.register(ProductModel,ProductAdmin)

class ArticleAdmin(admin.ModelAdmin):
    
    list_display=['name','articleCode','articleImage','created']
admin.site.register(ArticleModel,ArticleAdmin)