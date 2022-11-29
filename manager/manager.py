import datetime
import time

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from manager.models import resident, manager, suggestion, worker, payment, newsmessage

def Logout(request):
    logout(request)
    return redirect("/login/")

def index(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    return render(request, "manager/manager.html")


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
    user = manager.objects.get(mnum=usernum)
    trans = {
        "mnum" :hello2(user.mnum),
        "mname" :hello2(user.mname),
        "mtelnum" :hello2(user.mtelnum),
        "marea" :hello2(user.marea),
    }
    return render(request,"manager/mmessage.html",{"user":trans})
def hello(val):
    if val == "":
        return None
    else:
        return val
def changeMa(request):
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
    nepassword = hello(request.POST.get("newpassword"))
    telnum = hello2(request.POST.get("telnum"))
    area = hello2(request.POST.get("area"))
    man =manager.objects.get(mnum=num)
    man.mname = name
    if password is not None:
        man.mpassword = password
    man.mtelnum = telnum
    man.marea = area
    man.save()
    return redirect("/manager/message/")

def shownews(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    new1 = newsmessage.objects.all()
    return render(request, "manager/news.html", {"news":new1})

def changenews(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    print("hello")
    num = request.POST.get("cnum")
    title = request.POST.get("ctitle")
    contend = request.POST.get("ccontend")
    newsmsg = newsmessage.objects.get(newsnum=int(num))
    newsmsg.newstitle = hello(title)
    newsmsg.newscontend = hello(contend)
    newsmsg.save()
    return redirect("/manager/shownews/")


def addnews(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    title = request.POST.get("title")
    contend = request.POST.get("contend")
    newsmsg = newsmessage()
    newsmsg.newstitle = hello(title)
    newsmsg.newscontend = hello(contend)
    newsmsg.newsdate = datetime.datetime.now()
    newsmsg.save()
    return redirect("/manager/shownews/")

def deleteNew(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    new = newsmessage.objects.get(newsnum=num)
    new.delete()
    return JsonResponse({'result':"删除成功！"})

def allresident(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    allres = resident.objects.all()
    return render(request,"manager/allresident.html",{"resident":allres})


def changeRe(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    print(num)
    numc = int(request.POST.get("numc"))

    name = hello(request.POST.get("name"))
    password = request.POST.get("password")
    address = request.POST.get("address")
    contend = hello(request.POST.get("contend"))
    res1 = resident.objects.get(rnum=num)
    if num != numc:
        res2 =resident()
        res2.rnum = numc
        res2.rname = name
        res2.rpassword = password
        res2.raddress = address
        res2.rcontend = contend
        res2.rgender = res1.rgender
        res2.rtelnum = res1.rtelnum
        res2.rwechat = res1.rwechat
        res2.rqq = res1.rqq
        res2.rbirth = res1.rbirth
        res2.save()
        res1.delete()
    else:
        res1.rname = name
        res1.rpassword = password
        res1.raddress =address
        res1.rcontend = contend
        res1.save()
    return JsonResponse({'result': "修改成功"})

def deleteRe(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    res = resident.objects.get(rnum=num)
    res.delete()
    return JsonResponse({'result': "删除成功"})

def addRe(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    num = int(request.POST.get("num"))
    name = hello(request.POST.get("name"))
    password = request.POST.get("password")
    address = request.POST.get("address")
    contend = hello(request.POST.get("contend"))
    res = resident()
    res.rnum = num
    res.rname = name
    res.rpassword = password
    res.raddress = address
    res.rcontend = contend
    res.save()
    return JsonResponse({'result': "增加成功"})

def allworker(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    allwor = worker.objects.all()
    for w in allwor:
        if w.wtasknum is None:
            w.wtasknum = "无"
    return render(request,"manager/allworker.html",{"worker":allwor})

def changeWo(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    numc = int(request.POST.get("numc"))
    name = hello(request.POST.get("name"))
    password = request.POST.get("password")
    wor1 = worker.objects.get(wnum=num)
    if num != numc:
        wor2 = worker()
        wor2.wnum = numc
        wor2.wname = name
        wor2.wpassword = password
        wor2.save()
        wor1.delete()
    else:
        wor1.wname = name
        wor1.wpassword = password
        wor1.save()
    return JsonResponse({'result': "修改成功"})

def deleteWo(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    wor = worker.objects.get(wnum=num)
    wor.delete()
    return JsonResponse({'result': "删除成功"})

def addWo(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    num = int(request.POST.get("num"))
    name = request.POST.get("name")
    password = request.POST.get("password")
    wtype = request.POST.get("type")
    wor = worker()
    wor.wnum = num
    wor.wname = name
    wor.wpassword = password
    wor.wjoindate = datetime.datetime.now()
    wor.wtype = wtype
    wor.wtasknum = None
    wor.wtaskmount = 0
    wor.wholiday = "无"
    wor.save()
    return JsonResponse({'result': "增加成功"})

def allpayment(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    allpay = payment.objects.filter(paytype="3")
    return render(request,"manager/allpayment.html",{"payment":allpay})

def changePay(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    num = int(request.POST.get("num"))
    paysum = hello(request.POST.get("sum"))
    date = hello(request.POST.get("date"))
    dateTime = time.strptime(date, u"%Y年%m月%d日")
    publishTime = time.strftime("%Y-%m-%d", dateTime)
    paytype = hello(request.POST.get("type"))
    pay = payment.objects.get(id=num,paytype=paytype)
    pay.paysum = paysum
    pay.paydate = publishTime
    pay.save()
    return JsonResponse({"result":"修改成功"})

def allsuggestion(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束

    sug = suggestion.objects.all()
    return render(request, "manager/answer.html", {"suggestion": sug})

def answer(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        return redirect("/login/")
    # 判断登录结束
    suggestion_id = request.POST.get("id")
    answer_msg = request.POST.get("answer")
    sug = suggestion.objects.get(id=suggestion_id)
    answer_id = request.session.get("userId")
    sug.sanswer = answer_msg
    sug.sanum = answer_id
    sug.save()
    return JsonResponse({"result":"回答成功！"})
