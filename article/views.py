from django.views import View
from django.http import JsonResponse
from .models import ArticleModel, Styletag, ArticleCategory
import json
from utils import login_deco


class ArticleShow(View):
    
    @login_deco
    def get (self, request, category):
        
        if category == 'main' :
            data = ArticleModel.objects.all()
        
        elif category == 'wecodi' :
            target = ArticleCategory.objects.get(id=1)
            data = target.articlemodel_set.all()
        
        elif category == 'tip' :
            target = ArticleCategory.objects.get(id=2)
            data = target.articlemodel_set.all()

        else : 
            return JsonResponse ({"RESULT":"WRONG REQUEST"}, status=400)

        value=[]
        
        try: 
            for i in range(0,len(data)-1):
                innerVal = {}
                innerVal["title"] = data[i].title
                innerVal["categoryname"] = data[i].articleCategory.categoryname
                innerVal["thumb_img"] = data[i].thumb_img
                value.append(innerVal)

            return JsonResponse({"DATA":f"{value}","RESULT":"LOAD DONE"}, status=200)

        except:
            return JsonResponse({"RESULT":"ERROR"}, status=500)
