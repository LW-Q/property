
# 服务功能,维修、清洁等

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from manager.models import resident, demand,  worker, newsmessage

def news(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    userid = request.session.get("userId")
    new1 = newsmessage.objects.all()

    return render(request, "resident/slide/news.html", { "userid": userid, "news": new1})

def my_decorator(view_func):
    """
    定义装饰器，装饰类视图
    :param view_func: 被装饰的视图函数
    :return: wrapper，装饰的结果
    """

    def wrapper(request, *args, **kwargs):
        print(request.method, request.path)
        # 调用给装饰的视图函数
        return view_func(request, *args, **kwargs)

    return wrapper

def samef(user, dtype):
    dem = demand(drnum=user, dtype=dtype)
    if dem.dnum is None:
        return True
    else:
        return False

def clean(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    request.session["is_again"] = False
    return render(request, "resident/service/cleaning.html")

class door(View):
    @method_decorator(my_decorator, name='get')
    def get(self, request):
        # 是否登录
        is_login = request.session.get("is_login")
        if not is_login:
            request.session['is_return'] = True
            request.session.set_expiry(5)
            return redirect("/login/")
        # 判断登录结束
        request.session["is_again"] = False
        return render(request, "resident/service/door.html")

    @method_decorator(my_decorator, name='post')
    def post(self, request):
        userid = request.session.get("userId")
        user = resident.objects.get(rnum=userid)
        dtype = request.POST.get("type")
        dc = request.POST.get("contend")
        if samef(user, dtype) is False:
            return render(request, "resident/service/door.html", {
                "result": "已有该类型需求，请勿多次提交，如果修改请去全部需求查看"
            })
        if request.session["is_again"] is True:
            return render(request, "resident/service/door.html", {"result": "反复提交失败"})

        if dc is "":
            return render(request, "resident/service/door.html", {"result": "需求为空"})

        try:
            dem = demand()
            dem.dtype = dtype
            dem.dcontend = dc
            dem.drnum = user
            dem.is_accept = False
            dem.dwnum = None
            dem.save()
        except Exception as e:
            print(e)
            return render(request, "resident/service/door.html", { "result": "提交失败！"})
        request.session["is_again"] = True
        return redirect("/alldemand/")

class fault(View):
    @method_decorator(my_decorator, name='get')
    def get(self, request):
        # 是否登录
        is_login = request.session.get("is_login")
        if not is_login:
            request.session['is_return'] = True
            request.session.set_expiry(5)
            return redirect("/login/")
        # 判断登录结束
        request.session["is_again"] = False
        return render(request, "resident/service/fault.html")

class safe(View):
    @method_decorator(my_decorator, name='get')
    def get(self, request):
        # 是否登录
        is_login = request.session.get("is_login")
        if not is_login:
            request.session['is_return'] = True
            request.session.set_expiry(5)
            return redirect("/login/")
        # 判断登录结束
        request.session["is_again"] = False
        return render(request, "resident/service/safe.html")

    @method_decorator(my_decorator, name='post')
    def post(self, request):
        userid = request.session.get("userId")
        user = resident.objects.get(rnum=userid)
        dtype = request.POST.get("type")
        dc = request.POST.get("contend")
        print(dtype)
        print(user.rnum)
        if samef(user, dtype) is False:
            return render(request, "resident/service/safe.html", {
                "result": "已有该类型需求，请勿多次提交，如果修改请去全部需求查看"
            })
        if request.session["is_again"] is True:
            return render(request, "resident/service/safe.html", {"result": "反复提交失败"})
        if dc is "":
            return render(request, "resident/service/safe.html", {"result": "需求为空"})
        try:
            dem = demand()
            dem.dtype = dtype
            dem.dcontend = dc
            dem.drnum = user
            dem.is_accept = False
            dem.dwnum = None
            dem.save()
        except Exception as e:
            print(e)
            return render(request, "resident/service/safe.html", {"result": "提交失败！"})
        request.session["is_again"] = True
        return redirect("/alldemand/")


# 此处不太好需要修改，如已经接取的任务不呢给修改
# 还有就是应该加日期，处理的日期和发布的日期
# 超过几天没人接取就直接强制安排
# 工钱结算
def alldemand(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    userid = request.session.get("userId")
    user = resident.objects.get(rnum=userid)
    dem = demand.objects.filter(drnum=user)
    return render(request, "resident/service/alldemand.html", { "demand": dem})

def changedemand(request, num):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    dem = demand.objects.get(dnum=num)
    typename = dem.get_dtype_display()
    return render(request, "resident/service/changedemand.html",
                  {"dem": dem, "demandname": typename})

def change_post(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    userid = request.session.get("userId")
    user = resident.objects.get(rnum=userid)
    dtype = request.POST.get("type")
    dc = request.POST.get("contend")
    dem = demand.objects.get(drnum=user, dtype=dtype)
    dem.dcontend = dc
    dem.save()
    return redirect("/alldemand/")

def deletede(request, num):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    dem = demand.objects.get(dnum=num)
    dem.delete()
    return redirect("/alldemand/")

def choose(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    order_type = request.GET.get("order")
    if order_type is None:
        order_type = "wnum"
    print("服务员排序方式:"+order_type)
    tipTitle= request.GET.get("tipTitle")
    try:
        choWorker = worker.objects.filter(wskilled__contains=tipTitle).order_by(order_type)
    except Exception as e:
        print(e)
        choWorker = worker.objects.filter(wskilled__contains=tipTitle)
    return render(request,"resident/service/choose.html",{"worker":choWorker,"title":tipTitle})

def payService(request):
    wnum= request.GET.get("wnum")
    wor = worker.objects.get(wnum=wnum)
    paymoney = wor.whoursalary
    typ = wor.wtype
    ret = {
        "money":paymoney,
        "wornum":wnum,
        "type":typ
    }
    return render(request,"resident/service/payService.html",ret)

def payser_success(request):
    wnum = request.POST.get("paywnum")
    contend = request.POST.get("note")
    userid = request.session.get("userId")
    typ = request.POST.get("type")
    dem = demand(drnum_id=userid,dwnum=wnum,dcontend=contend,dtype=typ,is_accept=True)
    dem.save()
    return redirect("/alldemand/")