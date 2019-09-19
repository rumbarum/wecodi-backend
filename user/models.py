from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length       = 40)
    last_name  = models.CharField(max_length       = 50)
    email      = models.EmailField(max_length      = 100, unique = True)
    password   = models.CharField(max_length       = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now     = True)

    class Meta:
        ## 테이블 이름은 복수를 사용하는걸 저는 개인적으로 선호 합니다.
        db_table='users'
