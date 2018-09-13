from django.db import models
import django.utils.timezone as timezone

# Create your models here.
# 普通用户
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    objects = models.Manager()
    def __str__(self):
        return self.username
    
class WarningHistory(models.Model):
    warningtype = models.CharField(max_length=20)
    warningcontent = models.CharField(max_length=100)
    addtime = models.DateTimeField('保存日期', default = timezone.now)
    objects = models.Manager()      
    def __str__(self):
        return self.warningcontent