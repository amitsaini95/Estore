from django.shortcuts import render
from .models import ProductModel
# Create your views here.
def ProductListView(request):
    products=ProductModel.objects.all()
    context={'products':products}
    return render(request,"product/productlist.html",context)