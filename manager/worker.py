
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from manager.models import demand, worker


def index(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    request.session['status'] = 2
    userid = request.session.get("userId")
    wor = worker.objects.get(wnum=userid)
    wor.is_online = True
    wor.save()
    return render(request, "worker/worker.html")


def hello2(val):
    strr = ""
    if val is None:
        return strr
    else:
        return val

def message(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    usernum = request.session.get("userId")
    user = worker.objects.get(wnum=usernum)
    trans = {
        "wnum" :hello2(user.wnum),
        "wname" :hello2(user.wname),
        "wtype" :hello2(user.wtype),
        "wtypename" :hello2(user.get_wtype_display()),
        "wtasknum" : hello2(user.wtasknum),
        "wtaskmount" : hello2(user.wtaskmount),
        "wjoindate" : hello2(user.wjoindate),
        "wholiday" : hello2(user.wholiday),
    }
    return render(request,"worker/wmessage.html",{"user":trans})
def hello(val):
    if val == "":
        return None
    else:
        return val
def changeWo(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    num = hello(request.POST.get('num'))
    name = hello(request.POST.get("name"))
    password = hello(request.POST.get("password"))
    tasknum = hello(request.POST.get("tasknum"))
    taskmount = hello(request.POST.get("taskmount"))
    holiday = hello(request.POST.get("holiday"))
    wok =worker.objects.get(wnum=num)
    wok.wname = name
    if password is not None:
        wok.wpassword = password
    wok.wtasknum = tasknum
    wok.wtaskmount = taskmount
    wok.wholiday =holiday
    wok.save()
    return redirect("/worker/message/")

def Logout(request):

    usernum = request.session.get("userId")
    wor = worker.objects.get(wnum=usernum)
    wor.is_online = False
    wor.save()
    logout(request)
    return redirect("/login/")


def alltask(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    usernum = request.session.get("userId")
    wok = worker.objects.get(wnum=usernum)
    dem = demand.objects.filter(dtype=wok.wtype)
    return render(request, "worker/alltask.html", {"demand": dem,"worker":wok})

def gettask(request,num):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    dem = demand.objects.get(dnum=num)
    dem.is_accept = True
    usernum = request.session.get("userId")
    dem.dwnum = usernum
    print(dem.is_accept)
    dem.save()
    return redirect("/worker/alltask")

def showtask(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    usernum = request.session.get("userId")
    dem = demand.objects.filter(dwnum=usernum)
    return render(request,"worker/showtask.html",{"demand":dem})


def allMessage(request):
    userid = request.session.get("userId")
    wor = worker.objects.get(wnum=userid)
    return render(request,"worker/allMessage.html",{"wor":wor})

