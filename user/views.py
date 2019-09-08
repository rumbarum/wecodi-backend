import bcrypt
import datetime
import json
import jwt
from django.views import View
from django.http  import JsonResponse, HttpResponse
from datetime     import timedelta
from .models      import Users
from wecodi_backend.my_settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
       
            if Users.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)
            else:
                password= bytes(data["password"], "utf-8")
                hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

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
        password=data["password"]

        try: 
            exist_user = Users.objects.get(email = data["email"])

            if bcrypt.checkpw(password.encode("UTF-8"), exist_user.password.encode("UTF-8")):
                payload = { "user_id": exist_user.id,}
                encoded = jwt.encode(payload, f"{SECRET_KEY}", algorithm="HS256")

                return JsonResponse({"TOKEN": encoded.decode("UTF-8")}, status=200)
            else:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
        except Users.DoesNotExist:
            return JsonResponse({"message": "INVALID_EMAIL_ADDRESS"}, status=400)
    
