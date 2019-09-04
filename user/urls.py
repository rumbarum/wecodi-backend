from django.urls import path
from .views import * 

urlpatterns = [
    path("user/signup", Signup.as_view())
    path("user/login", Login.as_view())
]
