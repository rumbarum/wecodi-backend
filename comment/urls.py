from django.urls import path
from .views import CommentAddView, CommentGetView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('/comment/<int:article_id>', CommentView.as_view()),
]
