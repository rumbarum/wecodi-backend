import json
import random

from utils   import login_required
from .models import ArticleModel, ArticleCategory, Styletag, HeartCheck

from django.http  import JsonResponse, HttpResponse
from django.views import View

class ArticleCategoryView(View):
    def get(self, request):
        try:
            offset      = int(request.GET.get('offset','0'))
            limit       = int(request.GET.get('limit','9'))
            category_id = int(request.GET.get('category_id', None))
            styletag_id = int(request.GET.get('styletag_id', None))

            articles    = ArticleModel.objects
            total_count = ArticleModel.objects

            if category_id or styletag_id:
                if category_id :
                    article_category = ArticleCategory.objects.get(id = category_id)
                    articles         = articles.filter(article_category = article_category)
                    total_count      = total_count.filter(article_category = article_category)

                if styletag_id:
                    style_tag   = StyleTag.objects.get(id = styletag_id)
                    articles    = articles.filter(styletag = style_tag)
                    total_count = total_count.filter(styletag = style_tag)

                articles    = articles[offset:limit]
                total_count = total_count.count()
            else:
                articles    = articles.all()[offset:limit]
                total_count = total_count.all().count()

            result = [{
                "article_id"    : article.id,
                "title"         : article.title ,
                "category_name" : article.article_category.name,
                "thumb_img"     : article.thumb_img,
            } for article in articles ]
        
            return JsonResponse({
                "articles"    : result,
                "total_count" : total_count
            }, status=200)
        except ValueError:
            return JsonResponse({"ERROR":"INVALID_QUERY_VALUE"}, status=400)
        except ArticleCategory.DoesNotExist: 
            return JsonResponse({"ERROR":"INVALID_CATEGORY"}, status=400)

class ArticleDetailView(View):
    @login_required
    def get(self, request, article_id):
        try:
            target  = ArticleModel.objects.get(id = article_id)
            article = {
                'TITLE'      : target.title,
                'CATEGORY'   : target.article_category.name,
                'CONTENT'    : target.content, # 데이터 정리는 따로 실행해야한다.
                'CREATED_AT' : target.created_at,
                'UPDATED_AT' : target.updated_at,
            }

            return JsonResponse({"data" : article}, status=200)
        except ArticleModel.DoesNotExist:
            return JsonResponse({"ERROR":"NO_ARTICLE"}, status=400)

class ArticleRecommendView(View):
    def get(self, request, article_id):
        try:
            quantity = int(request.GET.get("quantity","3"))
            target   = ArticleModel.objects.get(id = article_id)

            recommended_articles = ArticleModel.objects.filter(
                styletag_id          = target.styletag_id,
                id                  != article_id,
                article_category_id != target.article_category.id
            )

            if len(recommended_articles) > quantity:  
                recommended_articles = random.sample(list(recommended_articles), quantity)
            
            recommended_articles = [{
                "article_id" : article.id,
                "title"      : article.title,
                "thumb_img"  : article.thumb_img,
                "category"   : article.articleCategory.name,
                "styletag"   : article.styletag.name
            } for article in recommended_articles] 
            
            return JsonResponse({"data" : recommended_articles}, status=200)
        except ValueError:
            return JsonRespone({"RESULT":"INPUT_QUERY_NUMBER"}, status=400)
        except ArticleModel.DoesNotExist:
            return JsonResponse({"RESULT":"WRONG_ARTICLE_ID"}, status=400) 

class HeartCheckView(View):
    @login_required
    def get(self,request, article_id):
        user_id = request.user.id
        article = ArticleModel.objects.filter(id            = article_id)
        target  = HeartCheck.objects.filter(articlemodel_id = article_id)
        heart   = target.filter(users_id                    = user_id)

        if article.exists():
            if target.filter(users_id=user_id).exists():
                return JsonResponse({"HEART_CHECK":"HEART_ON", "HEART_COUNT" : len(target)}, status=200)
            else:
                 return JsonResponse({"HEART_CHECK":"HEART_OFF", "HEART_COUNT" : len(target)}, status=200) 
        else: 
            return JsonResponse({"ERROR": "NO_ARTICLE"}, status=404) 

    @login_required
    def post(self, request, article_id ): 
        user_id    = request.user.id
        article    = ArticleModel.objects.filter(id            = article_id)
        target     = HeartCheck.objects.filter(articlemodel_id = article_id)
        del_target = HeartCheck.objects.filter(articlemodel_id = article_id, users_id = user_id)

        if article.exists():
            if del_target.exists():
                del_target[0].delete()  
                return JsonResponse ({"HEART_CHECK":"HEART_OFF", "HEART_COUNT":len(target)}, status=200)
            else: 
                HeartCheck(users_id=user_id, articlemodel_id=article_id).save()
                return JsonResponse({"HEART_CHECK":"HEART_ON", "HEART_COUNT":len(target)}, status=200)
        else:
            return JsonResponse({"RESULT":"NO_ARTICLE"}, status=400) 
