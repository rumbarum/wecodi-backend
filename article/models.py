from django.db import models
from user.models import Users

class ArticleModel (models.Model):
    title           = models.CharField(max_length                    = 500)
    articleCategory = models.ForeignKey('ArticleCategory', on_delete = models.PROTECT)
    content         = models.TextField()
    created_at      = models.DateTimeField(auto_now                  = True)
    updated_at      = models.DateTimeField(auto_now_add              = True)
    thumb_img       = models.URLField(max_length                     = 2500)
    styletag        = models.ForeignKey('Styletag', on_delete        = models.PROTECT)

    class Meta:
        db_table = 'articles'

class Styletag(models.Model): 
    name       = models.CharField(max_length   = 50)
    created_at = models.DateTimeField(auto_now = True)
    
    class Meta: 
        db_table = 'style_tags'

class ArticleCategory (models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'article_categories'

class HeartCheck(models.Model):
    users         = models.ForeignKey(Users, on_delete        = models.CASCADE)
    article_model = models.ForeignKey(ArticleModel, on_delete = models.CASCADE)
    created_at    = models.DateTimeField(auto_now             = True)
    
    class Meta:
        db_table = 'hearts'
