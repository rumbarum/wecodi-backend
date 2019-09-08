from django.urls import path, include

urlpatterns = [
    path('article', include('article.urls')),
    path('user', include('user.urls')),
    path('comment', include('comment.urls')),
]
