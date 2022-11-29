from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from manager.models import resident, manager, worker, payment, suggestion


def login(request):
    if request.session.get("is_return") is True:
        request.session.set_expiry(5)
        return render(request, "login.html", {"script": "alert", "wrong": "未登录"})
    return render(request, "login.html")

def index(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    '''
        接入水电费接口，查询户号对应的水电费等费用
        插入数据库中，下方直接查询
    '''
    userid = request.session.get("userId")
    user = resident.objects.get(rnum=userid)
    user.is_online =True
    user.save()
    paymoney = payment.objects.filter(paypeople_id=userid)
    water = paymoney.get(paytype='1')
    electricity = paymoney.get(paytype='2')
    propay = paymoney.get(paytype='3')
    request.session['status'] = 1
    return render(request, "resident/resident.html",
                  {"userid": userid, "water": water, "electricity": electricity,
                   "propay": propay})

def doLogin(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    statu = request.POST.get('status')
    if statu == "1":  # 业主登录
        try:
            res = resident.objects.get(rnum=user)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "4"})
        if res.rpassword != password:
            return JsonResponse({"status": "5"})
        request.session['is_login'] = True
        request.session['statu'] = statu
        request.session['userName'] = res.rname
        request.session['userId'] = res.rnum
        return JsonResponse({"status": "1"})

    if statu == "2":  # 工人登录
        try:
            wor = worker.objects.get(wnum=user)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "4"})
        if wor.wpassword != password:
            return JsonResponse({"status": "5"})
        request.session['is_login'] = True
        request.session['statu'] = statu
        request.session['userName'] = wor.wname
        request.session['userId'] = wor.wnum
        return JsonResponse({"status": "2"})
    if statu == "3":  # 工人登录
        try:
            man = manager.objects.get(mnum=user)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "4"})
        if man.mpassword != password:
            return JsonResponse({"status": "5"})
        request.session['is_login'] = True
        request.session['statu'] = statu
        request.session['userName'] = man.mname
        request.session['userId'] = man.mnum
        return JsonResponse({"status": "3"})

def Logout(request):
    userid = request.session.get("userId")
    user = resident.objects.get(rnum=userid)
    user.is_online = False
    user.save()
    logout(request)
    return redirect("/login/")

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
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    usernum = request.session.get("userId")
    user = resident.objects.get(rnum=usernum)
    num = hello2(user.rnum)
    name = hello2(user.rname)
    password = hello2(user.rpassword)
    gender = hello2(user.rgender)
    address = hello2(user.raddress)
    telnum = hello2(user.rtelnum)
    wechat = hello2(user.rwechat)
    qq = hello2(user.rqq)
    contend = hello2(user.rcontend)
    birth = hello2(user.rbirth)

    trans = {
        "rnum": num,
        "rname": name,
        "rpassword": password,
        "rgender": gender,
        "raddress": address,
        "rtelnum": telnum,
        "rwechat": wechat,
        "rqq": qq,
        "rcontend": contend,
        "rbirth": birth
    }
    return render(request, "resident/rmessage.html",{"user": trans})

def hello(val):
    if val == "":
        return None
    else:
        return val

def changeRe(request):
    num = hello(request.POST.get('num'))
    name = hello(request.POST.get("name"))
    password = hello(request.POST.get("password"))
    nepassword = hello(request.POST.get("newpassword"))
    gender = hello(request.POST.get("gender"))
    address = hello(request.POST.get("address"))
    telnum = hello(request.POST.get("telnum"))
    wechat = hello(request.POST.get("wechat"))
    qq = hello(request.POST.get("qq"))
    contend = hello(request.POST.get("contend"))
    birth = hello(request.POST.get("birth"))
    res = hello(resident.objects.get(rnum=num))
    res.rname = name
    if password is not None:
        res.rpassword = password
    res.rgender = gender
    res.rtelnum = telnum
    res.rwechat = wechat
    res.rqq = qq
    res.rcontend = contend
    res.rbirth = birth
    res.save()
    return redirect("/message/")



def suggest(request):
    # contend = request.POST.get("contend")
    # userid = request.session.get("userId")
    # sgt = suggestion()
    # sgt.scontend = contend
    # sgt.snum = userid
    # sgt.save()
    return render(request,"resident/slide/suggest.html")

