from django.urls import path
from store.controller.views import Index, cart
from store.controller.login import Login, logout
from store.controller.signup import signUp

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', signUp, name="signup"),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', cart, name= 'cart')
]
