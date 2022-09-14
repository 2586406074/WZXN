from django.db import models

# Create your models here.


# 用以登录的用户账号
class UserLogin(models.Model):
    # user_id = models.CharField(max_length=10)
    user_name = models.CharField(max_length=30)
    user_pwd = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=30)
    ident = models.IntegerField(choices=[(1, "已激活"), (2, "未激活")], default=1)  # 激活标识
    power = models.IntegerField(choices=[(1, "普通用户"), (2, "会员"), (3, "超级会员")], default=1)  # 身份标识
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间


# 地址信息
class Address(models.Model):
    # address_id = models.CharField(max_length=100)
    address_name = models.CharField(max_length=30)  # 收件地址
    nickname = models.CharField(max_length=30)  # 收件人，可以是昵称
    code = models.IntegerField()  # 邮编
    iphone = models.CharField(max_length=11)
    is_default = models.IntegerField(default=1)
    user_id = models.ForeignKey(to="UserLogin", on_delete=models.CASCADE)


# 购物车清单

class Shopping(models.Model):
    shopping_name = models.CharField(max_length=36)
    shopping_img = models.ImageField()
    shopping_price = models.CharField(max_length=32)
    shopping_des = models.CharField(max_length=64)
    # shopping_unit = models.CharField(max_length=12)

    shopping_id = models.ForeignKey(to="UserLogin", on_delete=models.CASCADE)





