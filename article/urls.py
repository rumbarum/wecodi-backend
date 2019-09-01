from django.urls import path
from .views import ArticleShow

urlpatterns = [
    path('/<int:category_id>/<int:pg_num>', ArticleShow.as_view()),
]
