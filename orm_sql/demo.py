# File Name :
# Description :
# Author : SYP
# date :


import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WZXN.settings")
    import django
    django.setup()
    # from user_app import models

    # my_db_obj = models.UserLogin.objects.create(user_name="qwe", user_pwd=111,user_email=123, ident=111, power=1)
    # my_db_obj = models.UserLogin.objects.filter(user_name="qwe")
    # my_db_obj[0].name = "asd"
    # my_db_obj[0].save()

    # my_user_obj = models.UserLogin.objects.all()
    # print(my_user_obj)


    from user_app import models
    # my_goods = models.Goods.objects.create(goods_name="手工产品")
    # my_goods.save()
    # my_goods_obj = models.Goods.objects.all()
    # print(my_goods_obj)

    # my_goods = models.AgricultureProducts.objects.create(agr_name="乡宁核桃", price="99", img="/static/images/agr/walnut.png", stock=100, state=1, des="2022年新货核桃薄皮乡宁纸皮核桃仁新鲜孕妇坚果薄壳散装坚果", goods_id_id=1)  # 添加农产品
    # my_goods.save()
    # my_goods_obg = models.Goods.objects.get(goods="农产")
    # print(my_goods_obg)

    user_data = models.Address.objects.create(address_name="山西省晋中市米加优", nickname="吴彦祖", code="11111", iphone="12312312312", user_id_id=11)
    user_data.save()
