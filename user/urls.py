from django.urls import path
## 귀찮더라도 * 를 사용해서 전부 import 하는것은 지양하세요.
## 의도치 않게 이름 충돌이 일어날 수 있습니다. 
from .views import SignUpView, LogInView

urlpatterns = [
    path("/signup", SignUpView.as_view()),
    path("/login", LogInView.as_view()),
]
