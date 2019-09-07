from django.db import models

class UserModel(models.Model):
    user_id = models.CharField(max_length=40)
    user_pw = models.CharField(max_length=40)
