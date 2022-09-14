import hashlib
import json
import math

from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_app.models import Shopping, UserLogin, Address
from scenic_spot.models import yunqiu

from goods.models import AgricultureProducts, Alcohol, Product, Goods
# Create your views here.


# 装饰器，判断是否有cookies值，如果有，则转入响应链接，否则，转入登录界面
def login_define(fn):

    def inner(request, *args, **kwargs):
        if not request.COOKIES.get("is_login"):
            path = request.path_info
            # print(next)
            return redirect("/login/?path={}".format(path))

        return fn(request, *args, **kwargs)
    return inner





# 二级界面
def goods(request):
    # agr_obj = AgricultureProducts.objects.all()
    # alc_obj = Alcohol.objects.all()
    #
    # return render(request, "second.html", {"arg_obj": agr_obj, "alc_obj": alc_obj})

    if request.method == 'GET':
        num = request.GET.get('page')
        if num:
            num = int(num)
        else:
            num = 1
            # print(num)
        # all_obj = Goods.objects.all()
        all_obj = AgricultureProducts.objects.all()
        pager = Paginator(all_obj, 4)
        pager_goodList = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

            # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:  # pager.num_pages获取的是总页数
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pagelist = range(begin, end + 1)
        return render(request, "second.html",
                      {"arg_obj": all_obj, "goodsList": pager_goodList, "currentnum": num, 'pagelist': pagelist})

def goods_rongzi(request):
    # agr_obj = AgricultureProducts.objects.all()
    # alc_obj = Alcohol.objects.all()
    #
    # return render(request, "second.html", {"arg_obj": agr_obj, "alc_obj": alc_obj})

    if request.method == 'GET':
        num = request.GET.get('page')
        if num:
            num = int(num)
        else:
            num = 1
            # print(num)
        # all_obj = Goods.objects.all()
        all_obj = Alcohol.objects.all()
        pager = Paginator(all_obj, 4)
        pager_goodList = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

            # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:  # pager.num_pages获取的是总页数
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pagelist = range(begin, end + 1)
        return render(request, "second_rongzi.html",
                      {"arg_obj": all_obj, "goodsList": pager_goodList, "currentnum": num, 'pagelist': pagelist})


def goods_spot(request):
    # agr_obj = AgricultureProducts.objects.all()
    # alc_obj = Alcohol.objects.all()
    #
    # return render(request, "second.html", {"arg_obj": agr_obj, "alc_obj": alc_obj})

    if request.method == 'GET':
        num = request.GET.get('page')
        if num:
            num = int(num)
        else:
            num = 1
            # print(num)
        # all_obj = Goods.objects.all()
        all_obj = Alcohol.objects.all()
        pager = Paginator(all_obj, 4)
        pager_goodList = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

            # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:  # pager.num_pages获取的是总页数
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pagelist = range(begin, end + 1)
        return render(request, "second_spot.html",
                      {"arg_obj": all_obj, "goodsList": pager_goodList, "currentnum": num, 'pagelist': pagelist})



# 从二级界面获取商品信息
@csrf_exempt
def get_data(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        img = data["img"]
        price = data["price"]
        des = data["des"]
        stock = data["stock"]
        name = data["name"]
        print(img, price, des, stock, name)
        # return redirect(f"/third?img={img}&price={price}&des={des}&stock={stock}")
        return HttpResponse("成功")


# 三级界面
@csrf_exempt
def third(request):
    if request.method == "POST":
        data = request.POST
        img = data["img"]
        price = data["price"]
        des = data["des"]
        stock = data["stock"]
        name = data["name"]
        oper = data["oper"]
        print(img, price, des, stock, oper, name)
        if oper == "加入购物车":
            if request.COOKIES.get("is_login"):

                user_name = request.COOKIES.get("is_login")
                print(user_name)
                user_obj = UserLogin.objects.filter(user_name=user_name).first()
                id = user_obj.id
                print(user_obj, id)
                # shopping_obj = Shopping.objects.all()
                Shopping.objects.create(shopping_name=name, shopping_price=price, shopping_img=img, shopping_des=des, shopping_id_id=id)

                # 构造json数据返回前端
                json_temp = {"flag": "加入购物车"}
                json_response = json.dumps(json_temp)

                return HttpResponse(json_response)

            else:
                path = request.path_info
                print(path)
                json_temp = {"flag": f"/login?path={path}&img={img}&price={price}&des={des}&stock={stock}&name={name}"}

                json_response = json.dumps(json_temp)
                return HttpResponse(json_response)

        else:

            json_temp = {"flag": "购买"}
            json_response = json.dumps(json_temp)
            return HttpResponse(json_response)

    img = request.GET.get('img')
    price = request.GET.get('price')
    des = request.GET.get('des')
    stock = request.GET.get('stock')
    name = request.GET.get('name')
    print(img, price, des, stock, name)
    return render(request, "third.html", {"img": img, "price": price, "des": des, "stock": stock, "name": name})


# 购物车
# 三级页面携带信息转入购物车界面
@login_define
def shopping_cart(request):
    if request.method == "POST":
        num = request.POST.get("num")
        if num == "添加数据库":
            name = request.POST.get("name")
            img = request.POST.get("img")
            price = request.POST.get("price")
            des = request.POST.get("des")
            print(name, img, price, des)
            user_name = request.COOKIES.get("is_login")
            print(user_name)
            user_id = UserLogin.objects.filter(user_name=user_name).first().id

            Shopping.objects.create(shopping_name=name, shopping_img=img, shopping_price=price, shopping_des=des,
                                    shopping_id_id=user_id)


        else:
            num = int(num)
            print(num)
            user_name = request.COOKIES.get("is_login")
            user_id = UserLogin.objects.filter(user_name=user_name).first()
            goods_objs = Shopping.objects.filter(shopping_id_id=user_id)
            print(goods_objs)

            goods_objs[num].delete()


    agr_obj = AgricultureProducts.objects.all()
    # print(agr_obj)

    user_name = request.COOKIES.get("is_login")
    # print(user_name)

    user_id = UserLogin.objects.filter(user_name=user_name).first()
    goods_objs = Shopping.objects.filter(shopping_id_id=user_id)

    # print(goods_objs)

    return render(request, "shopping_cart.html", {"goods_objs": goods_objs, "agr_obj": agr_obj})


# 订单界面
@login_define
def order(request):

    img = request.GET.get('img')
    price = request.GET.get('price')
    des = request.GET.get('des')
    stock = request.GET.get('stock')
    name = request.GET.get('name')
    print(img, price, des, stock)
    user_name = request.COOKIES.get("is_login")
    id = UserLogin.objects.filter(user_name=user_name).first().id
    print(id)
    address_obj = Address.objects.filter(user_id_id=id).first()
    print(address_obj)

    return render(request, "order.html", {"img": img, "name": name, "price": price,
                                          "des": des, "stock": stock, "address_obj": address_obj})



@csrf_exempt
def test(request):

    if request.method == "POST":
        num = request.POST.get("num")
        if num == "添加数据库":
            name = request.POST.get("name")
            img = request.POST.get("img")
            price = request.POST.get("price")
            des = request.POST.get("des")
            print(name, img, price, des)
            user_name = request.COOKIES.get("is_login")
            print(user_name)
            user_id = UserLogin.objects.filter(user_name=user_name).first().id

            Shopping.objects.create(shopping_name=name, shopping_img=img, shopping_price=price, shopping_des=des, shopping_id_id=user_id)


        else:
            # num = int(num)
            print(num)
            user_name = request.COOKIES.get("is_login")
            user_id = UserLogin.objects.filter(user_name=user_name).first()
            goods_objs = Shopping.objects.filter(shopping_id_id=user_id)
            print(goods_objs)
            n = 0
            for i in goods_objs:

                if n == num:
                    print(i)
                    i.delete()
                n += 1

    agr_obj = AgricultureProducts.objects.all()
    # print(agr_obj)

    user_name = request.COOKIES.get("is_login")
    # print(user_name)

    user_id = UserLogin.objects.filter(user_name=user_name).first()
    goods_objs = Shopping.objects.filter(shopping_id_id=user_id)

    # print(goods_objs)

    return render(request, "test.html", {"goods_objs": goods_objs, "agr_obj": agr_obj})



