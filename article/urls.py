from django.urls import path
from .views import ArticleView, ArticleDetailView, HeartCheckView,ArticleRecommendView

urlpatterns = [
    path('/category/<int:category_id>', ArticleView.as_view()),
    path('/detail/<int:article_id>',ArticleDetailView.as_view()),
    path('/heartcheck/<int:article_id>',HeartCheckView.as_view()),
    path('/recommend/<int:article_id>',ArticleRecommendView.as_view()),
]
