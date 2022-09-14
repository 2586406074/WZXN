from django.contrib import admin

from user_app.models import UserLogin
# Register your models here.


class User_info(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_pwd']


admin.site.register(UserLogin, User_info)



