from django.urls import path
from .views import ArticleCategoryView, ArticleDetailView, HeartCheckView, ArticleRecommendView, ArticleAllCategoryView

urlpatterns = [
    path('/allcategory', ArticleAllCategoryView.as_view()),
    path('/category/<int:category_id>', ArticleCategoryView.as_view()),
    path('/sort/<int:category_id>/<int:styletag_id>')
    path('/detail/<int:article_id>',ArticleDetailView.as_view()),
    path('/heartcheck/<int:article_id>',HeartCheckView.as_view()),
    path('/recommend/<int:article_id>',ArticleRecommendView.as_view()),
]
