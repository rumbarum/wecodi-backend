import json
import bcrypt
import jwt
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Users

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        password= bytes(data['password'], "utf-8")
        hashed_password = bcrpyt.hashpw(password, bcrypy.gensalt())

        user = Users(
                first_name=data["first_name"], 
                last_name=data["last_name"], 
                email=data["email"]
                )
        user.save()

        try: 
            return JsonResponse({"message":"SUCCESS"}, status=200)
        except:
            return JsonResponse({"message": ""}, status=400)

    def get(self, request):
        user = list(Users.objects.values())
        return JsonResponse(user, safe=False, status=200)

class LogInView(View):
    def post(self, request):
        data =json.loads(request.body)
        email=data["email"]
        password=data["password"]
        
        if

