import bcrypt
import datetime
import json
import jwt
import pdb

from django.views import View
from django.http  import JsonResponse, HttpResponse
from datetime     import timedelta
from .models      import Users
from wecodi_backend.my_settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
       
            print(data)
            
            if Users.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)
            else:
                print("else")
                password= bytes(data["password"], "utf-8")
                hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

                print(hashed_password)

                user = Users(
                    first_name=data["first_name"], 
                    last_name=data["last_name"], 
                    email=data["email"],
                    password = hashed_password.decode("utf-8"),
                )
                user.save()
                return JsonResponse({"message":"SUCCESS"}, status=200)

        except:
            return JsonResponse({"message": "INVALID"}, status=400)

class LogInView(View):
    def post(self, request):
        data =json.loads(request.body)
        user_email=data["email"]
        password=data["password"]
        
        print(user_email)
        if Users.objects.filter(email = user_email).exists():
            exist_user = Users.objects.get(email = user_email)
        else:
            return JsonResponse({"message": "INVALID_EMAIL_ADDRESS"}, status=400)

        if bcrypt.checkpw(password.encode("UTF-8"), exist_user.password.encode("UTF-8")):
            payload = {
                "email": user_email,
                "exp" : datetime.utcnow() + timedelta(weeks=1)
            }
            encoded = jwt.encode(payload, "SECRET_KEY", algorithm="HS256")

            return JasonResponse({"access_token": token.decode("UTF-8")}, status=200)
        else:
            return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
