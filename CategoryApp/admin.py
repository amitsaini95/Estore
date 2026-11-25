from django.contrib import admin
from .models import CategoryModel
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    
    list_display=['name','slug','categoryImage','created']
admin.site.register(CategoryModel,CategoryAdmin)