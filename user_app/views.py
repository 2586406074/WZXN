import hashlib
import json

from django.shortcuts import render, HttpResponse, redirect
from user_app.models import UserLogin, Address
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def login_define(fn):

    def inner(request, *args, **kwargs):
        if not request.COOKIES.get("is_login"):
            path = request.path_info
            # print(next)
            return redirect("/login/?path={}".format(path))

        return fn(request, *args, **kwargs)
    return inner


# 退出，删除cookies
@login_define
def logout(request):
    ret = redirect("/login/")
    ret.delete_cookie("is_login")
    return ret


# 主页

# @login_define
def base(request):

    return render(request, "base.html")


# 登录
@csrf_exempt
def login(request):

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        print(user, pwd)

        # 将密码md5加密，以获得的加密后的密码进行比较
        # 创建md5对象
        m = hashlib.md5()
        b = pwd.encode(encoding='utf-8')
        m.update(b)
        pwd_md5 = m.hexdigest()
        print(user, pwd_md5)

        oper = request.POST.get('btn')
        print(oper)
        if oper == "登录":

            buf = UserLogin.objects.filter(user_name=user, user_pwd=pwd_md5)
            if buf:
                # 判断是否有增值路由
                url = request.GET.get("path")
                print(f"查看路由为:{url}")

                # 拼接url，在登录之后可以跳转到原有界面
                if request.GET.get("path"):
                    path = request.GET.get("path")
                    img = request.GET.get("img")
                    price = request.GET.get("price")
                    des = request.GET.get("des")
                    stock = request.GET.get("stock")
                    name = request.GET.get("name")
                    print(path, img, price, des, stock)
                    if img and price and des and stock :
                        path = path + "?" + "img=" + img + '&price=' + price + '&des=' + des + '&stock=' + stock + '&name=' + name
                    # path = request.GET.get("")
                    # path = request.path_info
                        print(path)
                        # if path:
                        ret = redirect(path)
                    else:
                        ret = redirect(path)
                else:
                    ret = redirect("/base/")

                # 设置cookies值
                ret.set_cookie("is_login", user)
                return ret
            else:
                # next = request.GET.get("path")
                return redirect("/login/")

        else:
            return redirect("/register/")

    return render(request, 'user/login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 构造前端传来的json数据

        name = request.POST.get("name")
        passwd = request.POST.get("pwd")
        email = request.POST.get("email")
        print("*"*50)
        print(name, passwd, email)
        if passwd is None and email is None:
            flag = UserLogin.objects.filter(user_name="syp")  # 判断数据库中是否有此用户
            print(flag)
            if flag:
                flag = True
                # 构造json数据返回前端
                json_temp = {"flag": flag}
                print(json_temp)
                json_response = json.dumps(json_temp)
                return HttpResponse(json_response)
            else:
                flag = False
                # 构造json数据返回前端
                json_temp = {"flag": flag}
                print(json_temp)
                json_response = json.dumps(json_temp)
                return HttpResponse(json_response)

        # 创建md5对象
        m = hashlib.md5()
        b = passwd.encode(encoding='utf-8')
        m.update(b)
        passwd_md5 = m.hexdigest()
        # passwd_md5 = passwd

        flag = UserLogin.objects.filter(user_name=name)  # 判断数据库中是否有此用户

        if flag:
            flag = False
        else:
            UserLogin.objects.create(user_name=name, user_pwd=passwd_md5, user_email=email)
            flag = True

        # 构造json数据返回前端
        json_temp = {"flag": flag}
        json_response = json.dumps(json_temp)
        return HttpResponse(json_response)
    return render(request, "user/register.html")


def index(request):
    return render(request, "user/index.html")


# def test(request):
#     return render(request,"user/试验.html")


# 个人中心
@login_define
def personal_center(request):

    user_name = request.COOKIES.get("is_login")
    user_data = UserLogin.objects.filter(user_name=user_name).first()
    user_id = user_data.id
    print(user_id)
    user_address = Address.objects.filter(user_id_id=user_id).first()
    print(user_address)

    return render(request, "user/personal_center.html", {"user_data":user_data, "user_address": user_address})


def address(request):
    return render(request, "user/address.html")