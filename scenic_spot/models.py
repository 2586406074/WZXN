from django.db import models

# Create your models here.


class Travel(models.Model):
    travel_name = models.CharField(max_length=30)
    travel_price = models.CharField(max_length=12)  # 景区票价
    travel_state = models.CharField(max_length=5)  # 景区票_库存


class yunqiu(models.Model):
    yunqiu_name = models.CharField(max_length=32)  # 景区名称
    yunqiu_img = models.ImageField()
    yunqiu_describe = models.CharField(max_length=1000)  # 云丘山内部景区描述
    yuqiu_id = models.ForeignKey(to='Travel', on_delete=models.CASCADE)


class rognzi(models.Model):
    rongzi_name = models.CharField(max_length=32)  # 景区名称
    rongzi_img = models.ImageField()
    rongzi_describe = models.CharField(max_length=128)  # 戎子酒庄内部景区描述
    rongzi_id = models.ForeignKey(to='Travel', on_delete=models.CASCADE)


class baishan(models.Model):
    baishan_name = models.CharField(max_length=32)  # 景区名称
    baishan_img = models.ImageField()
    baishan_describe = models.CharField(max_length=128)  # 柏山寺内部景区描述
    baishan_id = models.ForeignKey(to='Travel', on_delete=models.CASCADE)


class fengling(models.Model):
    fengling_name = models.CharField(max_length=32)  # 景区名称
    fengling_img = models.ImageField()
    fengling_describe = models.CharField(max_length=128)  # 峰岭内部景区描述
    fengling_id = models.ForeignKey(to='Travel', on_delete=models.CASCADE)


