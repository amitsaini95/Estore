from django.urls import path
from .import views
urlpatterns = [
    path('',views.ProductListView,name="ProductList")
]
