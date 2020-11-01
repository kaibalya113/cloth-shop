from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from store.models import Customer



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

        value = {
            'firstName' : firstName,
            'lastName' : lastName,
            'email' : email,
            'phone' : phone,
            'password': password
        }
        customer = Customer(firstName=firstName,
                            lastName=lastName,
                            phone=phone,
                            email=email,
                            password=password)

        firstNameErrorMessage = None
        lastNameErrorMessage = None
        phoneErrorMessage = None
        passwordErrorMessage = None
        emailErrorMessage = None

        #validation
        if not firstName:
            firstNameErrorMessage = "First name is required!"
        elif len(firstName) < 4:
            firstNameErrorMessage = "First name must be 4 characters long"

        if not lastName:
            lastNameErrorMessage = "Last name is required"
        elif len(lastName) < 4:
            lastNameErrorMessage = "Last name must be 4 characters long!"

        if not phone:
            phoneErrorMessage = "Phone number is required!"
        elif len(phone) < 10:
            phoneErrorMessage = "Number should contain 10 digits"

        if not password:
            passwordErrorMessage = "Password is required!"

        if customer.isEmailExist():
            emailErrorMessage = "Email address already registered!"

        if not firstNameErrorMessage and not lastNameErrorMessage and not phoneErrorMessage and not passwordErrorMessage:
            customer.password = make_password(customer.password)
            customer.register()


            #return render(request, "index.html")
            return redirect("homepage")
        else:
            data ={
                "firstname": firstNameErrorMessage,
                "lastname": lastNameErrorMessage,
                "phone": phoneErrorMessage,
                "password": passwordErrorMessage,
                "email": emailErrorMessage,
                'value' : value
            }
            return render(request, "signup.html", data)