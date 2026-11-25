from django.shortcuts import render
from .models import ProductModel
from CategoryApp.models import CategoryModel
# Create your views here.
def ProductListView(request):
    products=ProductModel.objects.all()
    context={'products':products}
    return render(request,"product/productlist.html",context)
def ProductDetailView(request,slug):
    productslug=ProductModel.objects.get(slug=slug)
    print(productslug)
    return render(request,'product/productdetails.html',context={'productslug':productslug})

def ProductCategoryView(request,slug):
    category=CategoryModel.objects.get(slug=slug)
    productcat=ProductModel.objects.filter(category=category)
    return render(request,"product/prodctCategoryList.html",context={'productcatgorieslist':productcat})