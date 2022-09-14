from django.db import models

# Create your models here.


# 特产信息表
class Goods(models.Model):
    goods_name = models.CharField(max_length=30)
    goods_des = models.CharField(max_length=200)


# 农产表
class AgricultureProducts(models.Model):

    agr_name = models.CharField(max_length=12)
    price = models.CharField(max_length=32)
    img = models.ImageField()
    unit = models.CharField(max_length=12)  # 单位（斤）
    stock = models.CharField(max_length=100)  # 农产库存
    state = models.IntegerField(choices=[(1, "有货"), (2, "无货")], default=1)  # 库存状态（有货没货)
    des = models.CharField(max_length=200)  # 农产描述
    goods_id = models.ForeignKey(to="Goods", on_delete=models.CASCADE)


# 戎子酒
class Alcohol(models.Model):
    alc_name = models.CharField(max_length=12)
    price = models.CharField(max_length=32)
    img = models.ImageField()
    unit = models.CharField(max_length=12)  # 单位（斤）
    stock = models.CharField(max_length=100)  # 农产库存
    state = models.IntegerField(choices=[(1, "有货"), (2, "无货")], default=1)  # 库存状态（有货没货)
    des = models.CharField(max_length=200)  # 农产描述
    goods_id = models.ForeignKey(to="Goods", on_delete=models.CASCADE)


# 手工食品
class Product(models.Model):
    pro_name = models.CharField(max_length=12)
    price = models.CharField(max_length=32)
    img = models.ImageField()
    unit = models.CharField(max_length=12)  # 单位（斤）
    stock = models.CharField(max_length=100)  # 农产库存
    state = models.IntegerField(choices=[(1, "有货"), (2, "无货")], default=1)  # 库存状态（有货没货)
    des = models.CharField(max_length=200)  # 农产描述
    goods_id = models.ForeignKey(to="Goods", on_delete=models.CASCADE)








