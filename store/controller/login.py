from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.getCustomerByEmail(email)
        # print("name id lsjflasj f: "+customer)
        errorMessage = None
        if customer:
            # check password
            try:
                flag = check_password(password, customer.password)
            except:
                flag = False
            if flag:
                request.session['customerId'] = customer.id
                request.session['customerEmail'] = customer.email
                return redirect("homepage")
            else:
                errorMessage = 'Email and password invalid!'
        else:
            errorMessage = 'Email and password invalid!'
        print(customer)
        return render(request, 'login.html', {'error': errorMessage})