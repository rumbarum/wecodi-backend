import json
from django.views import View
from django.http import JsonResponse
from .models import Users

class User(view):
    def post(self, request):
        data = json.loads(request.body)
        user = User(first_name=data["first_name"], last_name=data["last_name"], email=data["email"], password=["password"])
        user.save()
        return JsonResponse({"message":"SUCCESS!"}, status=200)

        def get(self, request):
            user = list(Users.objects.values())
            return JsonResponse(user, safe=False, status=200)
