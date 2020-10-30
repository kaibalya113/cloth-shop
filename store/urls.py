from django.urls import path
from store.controller.views import index, signUp

urlpatterns = [
    path('', index, name="homepage"),
    path('signup', signUp)
]
