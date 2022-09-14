from django.db import models

# Create your models here.


class Restaurant(models.Model):  # 主表为农家乐，从表会有两张，一张餐饮

    rest_name = models.CharField(max_length=12)


class Menu(models.Model):

    menu_name = models.CharField(max_length=12)
    menu_type = models.CharField(max_length=12)
    menu_price = models.CharField(max_length=12)
    menu_img = models.ImageField()
    rest_id = models.ForeignKey(to="Restaurant", on_delete=models.CASCADE)


class Hostel(models.Model):
    hostel_type = models.CharField(max_length=12)  # 住宿房间类型（2人间/三人间）
    hostel_img = models.ImageField()
    host_state = models.CharField(max_length=6)  # 注册房间状态
    rest_id = models.ForeignKey(to="Restaurant", on_delete=models.CASCADE)






