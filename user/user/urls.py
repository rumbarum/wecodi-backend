from django.urls import path, include
from .views import User

urlpatterns = [
    path("", User.as_view()),
]
