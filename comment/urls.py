from django.urls import path
from .views import CommentAddView, CommentGetView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('/add/<int:article_id>', CommentAddView.as_view()),
    path('/list/<int:article_id>', CommentGetView.as_view() ),
    path('/update/<int:article_id>',CommentUpdateView.as_view()),
    path('/delete/<int:article_id>',CommentDeleteView.as_view()),
]
