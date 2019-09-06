from django.urls import path
from .views import * 

urlpatterns = [
    path("/signup", SignUpView.as_view()),
    path("/login", LogInView.as_view()),
    #path("/kakaologin", KakaoLogInView.as_view())
    ]
