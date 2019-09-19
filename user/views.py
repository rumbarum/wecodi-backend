import bcrypt
import datetime
import json
import jwt

from django.views import View
from django.http  import JsonResponse, HttpResponse
from datetime     import timedelta
from .models      import Users
from my_settings  import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        ## Try Catch를 사용하기에는 어떤 exception을 잡아야 하는지
        ## 불명확 하기 때문에, 차라리 더 명확하게 likely한 케이스를
        ## 아래처럼 명시하고, try catch는 지우는게 어떨까요?
        if "email" not in data or "password" not in data:
            return JsonResponse({"message": "INVALID_INPUT"}, status=400)
   
        if Users.objects.filter(email = data["email"]).exists():
            return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)
        
        password        = bytes(data["password"], "utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        Users(
            first_name = data["first_name"],
            last_name  = data["last_name"],
            email      = data["email"],
            password   = hashed_password.decode("utf-8"),
        ).save()

        return JsonResponse({"message":"SUCCESS"}, status=200)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if "email" not in data or "password" not in data:
            return JsonResponse({"message": "INVALID_INPUT"}, status=400)
 
        try: 
            password   = data["password"]
            exist_user = Users.objects.get(email = data["email"])

            if bcrypt.checkpw(password.encode("UTF-8"), exist_user.password.encode("UTF-8")):
                payload = {"user_id": exist_user.id}
                encoded = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

                return JsonResponse({"TOKEN": encoded.decode("UTF-8")}, status=200)
            else:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
        except Users.DoesNotExist:
            return JsonResponse({"message": "INVALID_EMAIL_ADDRESS"}, status=401)
    
