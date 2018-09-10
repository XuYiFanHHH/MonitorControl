from django.db import models

# Create your models here.
# 普通用户
class OrdinaryUserInfo(models.Model):
    userName = models.CharField(max_length=20)
    passWord = models.CharField(max_length = 20)
    def __str__(self):
        return self.userName

# 管理员
class SystemUserInfo(models.Model):
    userName = models.CharField(max_length=20)
    passWord = models.CharField(max_length = 20)
    def __str__(self):
        return self.userName