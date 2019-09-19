from django.urls import path
from .views import ArticleCategoryView, ArticleDetailView, HeartCheckView, ArticleRecommendView, ArticleAllCategoryView, ArticleSortView

urlpatterns = [
    path('/article', ArticleCategoryView.as_view()),
    path('/article/<int:article_id>',ArticleDetailView.as_view()),
    path('/heartcheck/<int:article_id>',HeartCheckView.as_view()),
    path('/recommend/<int:article_id>',ArticleRecommendView.as_view()),
]
