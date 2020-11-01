from django.urls import path
from store.controller.views import Index
from store.controller.login import Login
from store.controller.signup import signUp

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', signUp, name="signup"),
    path('login', Login.as_view(), name='login')
]
