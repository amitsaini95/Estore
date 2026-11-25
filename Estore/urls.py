from django.urls import path
from .import views
urlpatterns = [
    path('',views.ProductListView,name="ProductList"),
    path('product/<slug:slug>/',views.ProductDetailView,name="productDetails"),
    path('category/<slug:slug>/',views.ProductCategoryView,name="productCategories")
]
