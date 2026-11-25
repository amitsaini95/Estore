from django.shortcuts import render

# Create your views here.
def ProductListView(request):
    return render(request,"product/productlist.html")