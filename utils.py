import jwt
from django.http import JsonResponse
import json
import wecodi_backend.my_settings as setting 
from user.models import Users


def login_required(func):

    def wrappor(self,request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({"RESULT":"NO TOKEN"}, status=400)

        encode = request.headers["Authorization"]

        try:
            decoded = jwt.decode(encode, f"{setting.SECRET_KEY}", algorithms="HS256")
            User = Users.objects.get(id=decoded["user_id"])
            request.user = User   

        except jwt.DecodeError:
            return JsonResponse({"RESULT":"INVALID_TOKEN"}, status=400)
        except Users.DoesNotExist: 
            return JsonResponse({"RESULT":"WRONG_ID"}, status=400)

        return func(self,request, *args, **kwargs)

    return wrappor 
