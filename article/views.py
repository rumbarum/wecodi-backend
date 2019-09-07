from django.views import View
from django.http import JsonResponse, HttpResponse 
from .models import ArticleModel, Styletag, ArticleCategory, HeartCheck
import json
from utils import login_required
import random

class ArticleAllCategoryView(View): 
    
    @login_required 
    def get(self, request): 
        try:
            offset = int(request.GET.get('offset','0'))
            limit = int(request.GET.get('limit','9'))
            data = ArticleModel.objects.all()[offset:limit]

            return_value = [{
                "article_id": ele.id,
                "title" : ele.title ,
                "categoryname" : ele.articleCategory.name,
                "thumb_img" : ele.thumb_img,
                } for ele in data ]
        
            if len(return_value) == 0: 
                return JsonResponse({"RESULT":"NO_MORE_PAGE"}, status=200)
            else:    
                return JsonResponse({"DATA":return_value, "RESULT":"LOADED"}, status=200)


        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)
        except ValueError:
            return JsonResponse({"RESULT":"INPUT_QUERY_NUMBER"}, status=400)

class ArticleCategoryView(View):    
    
    @login_required
    def get(self, request, category_id):
        try:
            offset = int(request.GET.get('offset','0'))
            limit = int(request.GET.get('limit','9'))                    
            select = ArticleCategory.objects.get(id=category_id)
            data = select.articlemodel_set.all()[offset:limit]  
             
            return_value = [{
                "article_id": ele.id,
                "title" : ele.title ,
                "categoryname" : ele.articleCategory.name,
                "thumb_img" : ele.thumb_img,
                } for ele in data ]
        
            if len(return_value) == 0: 
                return JsonResponse({"RESULT":"NO_MORE_PAGE"}, status=200)
            else:    
                return JsonResponse({"DATA":return_value, "RESULT":"LOADED"}, status=200)

        except ValueError:
            return JsonResponse({"RESULT":"INPUT_QUERY_NUMBER"}, status=400)
        except ArticleCategory.DoesNotExist: 
            return JsonResponse({"RESULT":"WRONG_REQUEST"}, status=400)
        except AttributeError: 
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)

class ArticleDetailView(View):

    @login_required
    def get(self, request, article_id):
        try:
            target = ArticleModel.objects.get(id=article_id)
                       
            val = {
                'TITLE': target.title,
                'CATEGORY': target.articleCategory.name,
                'CONTENT': target.content,
                'CREATED_AT': target.created_at,
                'UPDATED_AT': target.updated_at,
                }

            return JsonResponse({"RESULT":"LOAD_DONE","DATA":val}, status=200)

        except ArticleModel.DoesNotExist:
            return JsonResponse({"RESULT":"NO_ARTICLE"}, status=400)
        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)

class ArticleRecommendView(View):

    @login_required 
    def get(self, request, article_id):
        try:
            quantity = int(request.GET.get("quantity","3"))
            target = ArticleModel.objects.get(id=article_id)
            catch=list(ArticleModel.objects.filter(styletag_id=target.styletag_id).exclude(id=article_id))

            if len(catch) > quantity:  
                catch = random.sample(catch, quantity)
            
            val = [{
                "title": ele.title,
                "thumb_img": ele.thumb_img,
                "category": ele.articleCategory.name,
                "styletag": ele.styletag.name
                } for ele in catch] 
            
            return JsonResponse({"RESULT":"DONE", "DATA":val}, status=200)
        
        except ValueError:
            return JsonRespone({"RESULT":"INPUT_QUERY_NUMBER"}, status=400)
        except ArticleModel.NotExist:
            return JsonResponse({"RESULT":"WRONG_ARTICLE_ID"}, status=400) 
        except AttributeError:
            return HttpResponse(status=400)

class ArticleSortView(View):
    
    @login_required
    def get(self, request, category_id, styletag_id)
        try:
            offset = int(request.GET.get('offset','0'))
            limit = int(request.GET.get('limit','9'))                    
            select = ArticleCategory.objects.filter(articleCategory_id=category_id)
            data = select.filter(styletag_id=styletag_id)[offset:limit]  
             
            return_value = [{
                "article_id": ele.id,
                "title" : ele.title ,
                "categoryname" : ele.articleCategory.name,
                "thumb_img" : ele.thumb_img,
                } for ele in data ]
        
            if len(return_value) == 0: 
                return JsonResponse({"RESULT":"NO_MORE_PAGE"}, status=200)
            else:    
                return JsonResponse({"DATA":return_value, "RESULT":"LOADED"}, status=200)

        except ValueError:
            return JsonResponse({"RESULT":"INPUT_QUERY_NUMBER"}, status=400)
        except ArticleCategory.DoesNotExist: 
            return JsonResponse({"RESULT":"WRONG_REQUEST"}, status=400)
        except AttributeError: 
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)

class HeartCheckView(View):

    @login_required
    def get(self,request, article_id):
        user_id = request.user.id
        target = HeartCheck.objects.filter(articlemodel_id=article_id)
        heartcount = len(target)

        if target.filter(usermodel_id=user_id).exists():
            return JsonResponse({"HEART_CHECK":"HEART_ON", "HEART_COUNT":heartcount}, status=200)
        else:
            return JsonResponse({"HEART_CHECK":"HEART_OFF", "HEART_COUNT":heartcount}, status=200) 

    @login_required
    def post(self, request, article_id ): 
        user_id = request.user.id
        article = HeartCheck.objects.filter(articlemodel_id=article_id)
        heart = article.filter(usermodel_id=user_id) 

        if article.exists():
            if heart.exists():
                heart.delete()  
                return JsonResponse ({"HEART_CHECK":"HEART_OFF", "HEART_COUNT":len(article)}, status=200)
            else: 
                HeartCheck(usermodel_id=user_id, articlemodel_id=article_id).save()
                return JsonResponse({"HEART_CHECK":"HEART_ON", "HEART_COUNT":len(article)}, status=200)
        else:
            return JsonResponse({"RESULT":"NO_ARTICLE"}, status=400) 
