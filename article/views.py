from django.views import View
from django.http import JsonResponse, HttpResponse 
from .models import ArticleModel, Styletag, ArticleCategory, HeartCheck
import json
from utils import login_required
import random

class ArticleView(View):    
    @login_required
    def get (self, request, category_id):
        try:
            if category_id == 0:
                data = ArticleModel.objects.all()[int(request.GET.get("offset",'0')):int(request.GET.get("limit",'9'))]
            else:
                select = ArticleCategory.objects.get(id=category_id)
                data = select.articlemodel_set.all()[int(request.GET.get("offset",'0')):int(request.GET.get("limit",'9'))]  
             
            return_value = [{
                "article_id": ele.id,
                "title" : ele.title ,
                "categoryname" : ele.articleCategory.name,
                "thumb_img" : ele.thumb_img,} for ele in data ]
        
            if len(return_value)==0 : 
                return JsonResponse({"RESULT":"NO_MORE_PAGE"},status=200)
            else:    
                return JsonResponse({"DATA":f"{return_value}","RESULT":"LOADED"}, status=200)

        except ArticleCategory.DoesNotExist : 
            return JsonResponse ({"RESULT":"WRONG_REQUEST"}, status=400)
        except AttributeError : 
            return JsonResponse ({"RESULT":"WRONG_INPUT"},status=400)

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
                'UPDATED_AT': target.updated_at,}

            return JsonResponse({"RESULT":"LOAD_DONE","DATA":f"{val}"}, status=200)

        except ArticleModel.DoesNotExist:
            return JsonResponse({"RESULT":"NO_ARTICLE"}, status=400)
        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"},status=400)

class ArticleRecommendView(View):
    @login_required 
    def get (self, request, article_id):
        try:
            target = ArticleModel.objects.get(id=article_id)
            catch=list(ArticleModel.objects.filter(styletag_id=target.styletag_id).exclude(id=article_id))

            if len(catch)>int(request.GET.get("quantity",'3')):  
                catch = random.sample(catch, int(request.GET.get("quantity",'3')))
            
            val = [{
                "title": ele.title,
                "thumb_img": ele.thumb_img,
                "category": ele.articleCategory.name} for ele in catch]
            
            return JsonResponse ({"RESULT":"DONE","DATA":f"{val}"},status=200)
        except ArticleModel.DoesNotExist :
            return JsonResponse({"RESULT":"WRONG_ARTICLE_ID"},status=400) 
        except AttributeError:
            return HttpResponse(status=400)

class HeartCheckView(View):
    @login_required
    def get (self,request, article_id):
        try:
            heartcount = len(HeartCheck.objects.filter(articlemodel_id=article_id))
            if HeartCheck.objects.filter(usermodel_id=request.user.id ,articlemodel_id = article_id).exists():
                return JsonResponse({"HEART_CHECK":"HEART_ON","HEART_COUNT":f"{heartcount}"},status=200)
            else :
                return JsonResponse({"HEART_CHECK":"HEART_OFF","HEART_COUNT":f"{heartcount}"}, status=200) 
        
        except AttributeError :
            return JsonResponse ({"RESULT":"WRONG_INPUT"},status=400)

    @login_required
    def post (self, request, article_id ): 
        try: 
            user_id = request.user.id 
            if HeartCheck.objects.filter(usermodel_id=user_id ,articlemodel_id = article_id).exists():
                target = HeartCheck.objects.get(articlemodel_id=article_id , usermodel_id = user_id)
                target.delete()
                heartcount = len(HeartCheck.objects.filter(articlemodel_id=article_id))
                return JsonResponse ({"HEART_CHECK":"HEART_OFF","HEART_COUNT":f"{heartcount}"}, status=200)
            else : 
                if ArticleModel.objects.filter(id= article_id).exists():
                    target = HeartCheck(usermodel_id = user_id, articlemodel_id=article_id)
                    target.save()
                    heartcount = len(HeartCheck.objects.filter(articlemodel_id=article_id))
                    return JsonResponse({"HEART_CHECK":"HEART_ON","HEART_COUNT":f"{heartcount}"},status=200)
                else: 
                    return JsonResponse({"RESULT":"NO_ARTICLE"},status=400)
        except AttributeError:
            return HttpResponse(status=400)
