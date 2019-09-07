from django.views import View
from django.http import JsonResponse
from .models import UserModel
import json 
import jwt
import wecodi_backend.my_settings as settings


# 사인업 없음, 내가 회원정보 삽입
# 로그인 하면 토큰 주고 , 토크으로 데코레이터 확인만 한다. 

class UserLogin(View): 
    
    def post(self, request):
        req = json.loads(request.body) 

        try:
            User = UserModel.objects.get(user_id=req['user_id'])
            if req['user_pw'] == User.user_pw :
                target = User.user_id
                encoded = jwt.encode({"user_id":f"{target}"}, f"{settings.SECRET_KEY}", algorithm='HS256').decode('utf-8')
                return JsonResponse ({"TOKEN":f"{encoded}"}, status=200)
            else :
                return JsonResponse({"RESULT":"WRONG_PASSWORD"},status=400)

        except :   
            return JsonResponse ({"CODE":"ERROR"},status=400)

    def get(self, request):

        return JsonResponse({"message":"WORKING"}, status=500)
