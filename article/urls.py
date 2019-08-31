from django.urls import path
from .views import ArticleShow

urlpatterns = [
    path('/<str:category>', ArticleShow.as_view()),
]
