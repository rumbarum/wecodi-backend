from django.db import models
from user.models import Users
from article.models import ArticleModel

class CommentModel(models.Model):
    comment = models.TextField()
    deleted = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    articlemodel=models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    class Meta: 
        db_table = "Comment"
    
