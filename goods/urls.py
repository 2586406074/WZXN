"""WZXN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from goods import views


urlpatterns = [
    path("goods/", views.goods),  # 二级界面
    path("goods_rongzi/", views.goods_rongzi),
    path("goods_spot/", views.goods_spot),

    path("get_data/", views.get_data),  # 获取二级界面信息
    path("third/", views.third),  # 三级商品界面
    path("shopping_cart/", views.shopping_cart),  # 购物车界面
    path("order/", views.order),  # 订单界面

    path("test/", views.test),  # 测试界面



]
