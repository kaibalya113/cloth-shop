from builtins import filter

from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.
# def index(request):
#     category = Category.getAllCategories()
#     products = None
#     categoryId = request.GET.get('category')
#     if categoryId:
#         products = Product.getAllProductsById(categoryId)
#     else:
#         products = Product.getAllProducts()
#     data ={}
#     data['products'] = products
#     data['category'] = category
#     try:
#         print('you are: '+request.session.get('customerEmail'))
#     except:
#         print('you are: ')
#     return render(request, 'index.html', data)

class Index(View):
    def get(self, request):
        category = Category.getAllCategories()
        products = None
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.getAllProductsById(categoryId)
        else:
            products = Product.getAllProducts()
        data = {}
        data['products'] = products
        data['category'] = category
        try:
            print('you are: ' + request.session.get('customerEmail'))
        except:
            print('you are: ')
        return render(request, 'index.html', data)

    def post(self, request):
        productId = request.POST.get('product')

        cart = request.session.get('cart')
        if cart:
            quantity = cart[productId]
            if quantity:
                cart[productId] = quantity + 1
            else:
                cart[productId] = 1


        else:
            cart = {}
            cart[productId] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

# class Login(View):
#     def get(self, request):
#         return render(request, "login.html")
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         customer = Customer.getCustomerByEmail(email)
#         # print("name id lsjflasj f: "+customer)
#         errorMessage = None
#         if customer:
#             # check password
#             try:
#                 flag = check_password(password, customer.password)
#             except:
#                 flag = False
#             if flag:
#
#                 return redirect("homepage")
#             else:
#                 errorMessage = 'Email and password invalid!'
#         else:
#             errorMessage = 'Email and password invalid!'
#         print(customer)
#         return render(request, 'login.html', {'error': errorMessage})

# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         customer = Customer.getCustomerByEmail(email)
#         #print("name id lsjflasj f: "+customer)
#         errorMessage = None
#         if customer:
#             #check password
#             try:
#                 flag = check_password(password, customer.password)
#             except:
#                 flag = False
#             if flag:
#
#                 return redirect("homepage")
#             else:
#                 errorMessage = 'Email and password invalid!'
#         else:
#             errorMessage = 'Email and password invalid!'
#         print(customer)
#         return render(request, 'login.html',{'error': errorMessage})
