from builtins import filter

from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


# Create your views here.
def index(request):
    category = Category.getAllCategories()
    products = None
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.getAllProductsById(categoryId)
    else:
        products = Product.getAllProducts()
    data ={}
    data['products'] = products
    data['category'] = category
    return render(request, 'index.html', data)

def signUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        #postData = request.POST

        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        customer = Customer(firstName = firstName,
                            lastName = lastName,
                            phone = phone,
                            email = email,
                            password  = password)
        customer.register()
        return HttpResponse(request.POST.get('email'))