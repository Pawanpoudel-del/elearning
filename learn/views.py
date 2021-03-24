from django.shortcuts import render
from django.views.generic import ListView
from learn.models import Product
# Create your views here.
class ProductListView(ListView):
    template_name ='learn/productlist.html'
    model=Product
