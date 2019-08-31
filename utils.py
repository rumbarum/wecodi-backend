import jwt
from django.http import JsonResponse
import json
import wecodi_backend.my_settings as setting 
from user.models import UserModel


def login_deco(func):
    
    def wrappor(self,request, *args, **kwargs):
    
        if 'Authorization' not in request.headers:
            return JsonResponse({"RESULT":"NO TOKEN"}, status=400)
            
        encode = request.headers["Authorization"]

        try:
            decoded = jwt.decode(encode, f"{setting.SECRET_KEY}", algorithms="HS256")
            User = UserModel.objects.get(user_id=decoded["user_id"])
            request.user = User   
            
        except jwt.DecodeError:
            return JsonResponse({"RESULT":"INVALID TOKEN"}, status=400)

        except UserModel.DoesNotExist: 
            return JsonResponse({"RESULT":"WRONG ID"}, status=400)
        
        return func(self,request, *args, **kwargs)
  
        

    return wrappor 
