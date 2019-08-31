from django.db import models

class ArticleModel (models.Model):
    title = models.TextField()
    articleCategory = models.ForeignKey('ArticleCategory', on_delete=models.PROTECT)
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    thumb_img = models.TextField()
    styletag = models.ForeignKey('Styletag', on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'Article'


class Styletag(models.Model): 
    stylename = models.CharField(max_length=50)
    
    class Meta: 
        db_table = 'Styletag'


class ArticleCategory (models.Model):
    categoryname = models.CharField(max_length=50)

    class Meta:
        db_table = 'ArticleCategory'
