from django.views import View
from django.http import JsonResponse
from .models import ArticleModel, Styletag, ArticleCategory, HeartCheck
import json
from utils import login_required
import random

class ArticleShow(View):    
    @login_required
    def get (self, request, category_id, pg_num):
        try:
            if category_id == 0:
                data = ArticleModel.objects.all()[pg_num*9:pg_num*9+9]
            else:
                select = ArticleCategory.objects.get(id=category_id)
                data = select.articlemodel_set.all()[pg_num*9:pg_num*9+9]  
             
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
        except :
            return JsonResponse({"RESULT":"ERROR"}, status=500)

class ArticleDetail(View):
    @login_required
    def get(self, request, article_id):
        try:
            target = ArticleModel.objects.get(id=article_id)
            stylecatch=list(ArticleModel.objects.filter(styletag_id=target.styletag_id).exclude(id=article_id))
            if len(stylecatch)>5 : 
                stylecatch = random.sample(stylecatch,5)
            
            recommend = [{
                "article_id":ele.id,
                "title": ele.title,
                "thumb_img": ele.thumb_img
                } for ele in stylecatch ]
            
            try:
                HeartCheck.objects.get(usermodel_id=request.user.id ,articlemodel_id = article_id)
                heart = "ON"
            
            except :
                heart = "OFF"
            heartcounter = len(HeartCheck.objects.filter(articlemodel_id=article_id))
            val = {
                'TITLE': target.title,
                'CATEGORY': target.articleCategory.name,
                'CONTENT': target.content,
                'RECOMMEND': recommend,
                'CREATED_AT': target.created_at,
                'UPDATED_AT': target.updated_at,
                'HEART_CHECK': heart,
                'HEART_COUNTER': heartcounter,
                }
            return JsonResponse({"RESULT":"LOAD_DONE","DATA":f"{val}"}, status=200)

        except ArticleModel.DoesNotExist:
            return JsonResponse({"RESULT":"NO_ARTICLE"}, status=404)
        except ValueError:
            return JsonResponse({"RESULT":"NO_RECOMMEND"}, status=400)
        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"},status=400)
    
    @login_required
    def post ( self, request, article_id ):
        data = json.loads(request.body)
        user_id = request.user.id
        
        if data['HEART'] == "HEART_ON":
            try:
                HeartCheck.objects.get(usermodel_id=user_id, articlemodel_id=article_id)
                return JsonResponse({"RESULT":"ALREADY_ON"}, status=406)
            except HeartCheck.DoesNotExist :
                heart = HeartCheck(usermodel_id=user_id, articlemodel_id=article_id)
                heart.save() 
                return JsonResponse({"RESULT":"HEART_ON"}, status=200)
        
        if data['HEART'] == "HEART_OFF":
            try: 
                heart = HeartCheck.objects.get(usermodel_id=user_id, articlemodel_id=article_id)
                heart.delete()
                return JsonResponse({"RESULT":"HEART_OFF"},status=200)
            except HeartCheck.DoesNotExist:
                return JsonResponse({"RESULT":"WRONG_REQUEST"},status=400)
        else: 
            return JsonResponse({"RESULT":"WRONG_REQUEST"},status=400)
