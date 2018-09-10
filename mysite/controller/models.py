from django.db import models

# Create your models here.
# 普通用户
class UserInfo(models.Model):
    userName = models.CharField(max_length=20)
    passWord = models.CharField(max_length = 20)
    def __str__(self):
        return self.userName