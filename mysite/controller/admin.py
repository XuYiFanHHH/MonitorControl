from django.contrib import admin
from .models import UserInfo, WarningHistory

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(WarningHistory)
# 默认账号 admin, 密码xyfllppass