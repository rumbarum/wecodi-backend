from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/signup", SignUpView.as_view()),
    path("/login", LogInView.as_view()),
    #path("/kakaologin", KakaoLogInView.as_view())
    ]
