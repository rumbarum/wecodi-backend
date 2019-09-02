from django.urls import path
from .views import ArticleShow, ArticleDetail

urlpatterns = [
    path('/category=<int:category_id>/page=<int:pg_num>', ArticleShow.as_view()),
    path('/detail=<int:article_id>',ArticleDetail.as_view())
]
