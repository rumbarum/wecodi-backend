from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/signup", Signup.as_view()),
    path("user/login", Login.as_view()),
]
