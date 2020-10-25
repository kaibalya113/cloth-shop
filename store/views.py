from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product


# Create your views here.
def index(request):
    products = Product.getAllProducts()
    print(products)
    return render(request, 'index.html', {'products': products})