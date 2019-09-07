from django.views import View
from django.http import JsonResponse
from .models import ArticleModel, Styletag, ArticleCategory
import json
from utils import login_required

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
