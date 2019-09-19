from django.views import View
from django.http import JsonResponse, HttpResponse
from article.models import ArticleModel, Styletag, ArticleCategory, HeartCheck
from .models import CommentModel
import json
from utils import login_required

class CommentView(View):

    def get()...

    def delete()...

    @login_required
    def post(self, request, article_id):
        req = json.loads(request.body)
        comment_id = request.GET.get("comment_id", None)  
        user_id = request.user.id 

        try:
            if ArticleModel.objects.filter(id=article_id).exists(): 
                target = CommentModel(comment=req["comment"], 
                        articlemodel_id=article_id, users_id=user_id)
                target.save()
    
                val = {'id': target.id,
                        'comment': target.comment,
                        'user_name': target.users.last_name + target.users.first_name,
                        'updated_at': target.updated_at,
                        }
                
                return JsonResponse({"RESULT":"ADDED","DATA":val}, status=200)
            else:
                return JsonResponse({"RESULT":"NO_ARTICLE"}, stats=400)
        except AttributeError: 
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)

class CommentUpdateView(View):

    @login_required 
    def post (self, request, article_id ):
        req = json.loads(request.body)
        
        try: 
            if ArticleModel.objects.filter(id=article_id).exists():
                target = CommentModel.objects.get(id=req["comment_id"])
                target.comment = req["comment"]
                target.save()

                val = {'id': target.id,
                        'comment': target.comment,
                        'user_name': target.users.last_name + target.users.first_name ,
                        'updated_at': target.updated_at,
                        }

                return JsonResponse({"RESULT":"UPDATED","DATA":val}, status=200)
            else: 
                HttpResponse(status=404)
        except ValueError:
            return Jsonresponse({"RESULT":"WRONG_COMMENT_ID"}, status=400)
        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=400)

class CommentGetView(View):

    @login_required
    def get(self, request, article_id):
        try:
            if ArticleModel.objects.filter(id=article_id).exists():
                target = CommentModel.objects.filter(articlemodel_id=article_id)

                val = [{
                     "comment_id": ele.id,
                     "user_name": ele.users.last_name + ele.users.first_name,
                     "updated_at": ele.updated_at,
                     "comment": ele.comment,
                     } for ele in target if not ele.deleted]

                return JsonResponse({"DATA":val,"RESULT":"LOADED"}, status=200)
            else: 
                return JsonResponse({"RESULT":"NO_ARTICLE"}, status = 200)
        except AttributeError:
            return JsonResponse({"RESULT":"WRONG_INPUT"}, status=200)

class CommentDeleteView(View):

    @login_required 
    def post(self,request, article_id):
        req = json.loads(request.body)

        try:
            if ArticleModel.objects.filter(id=article_id).exists():
                target = CommentModel.objects.get(id=req["comment_id"])
                target.deleted = True
                target.save()
                return HttpResponse(status=200)    
            else:
                return JsonResponse({"RESULT":"NO_ARTICLE"}, status=400)
        except AttributeError: 
            return JsonResponse({"RRESULT":"WRONG_INPUT"}, status=400)
        except ValueError:
            return JsonResponse({"RESULT":"WRONG_COMMENT_ID"}, status=400)
        except CommentModel.DoesNotExist:
            return JsonResponse({"RESULT":"NO_COMMENT"}, status=400)
