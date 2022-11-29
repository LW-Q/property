#
# 缴费功能


from datetime import datetime
from django.shortcuts import render, redirect

from manager.models import  payment, bill

def pay(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    userid = request.session.get("userId")
    paymoney = payment.objects.filter(paypeople_id=userid)
    water = paymoney.get(paytype='1')
    electricity = paymoney.get(paytype='2')
    propay = paymoney.get(paytype='3')
    record = bill.objects.filter(people_id=userid).order_by("-date")
    wa = record.filter(type="1")
    mount = 0
    for w in wa:
        mount = mount + w.paymoney
    wall = {
        "num":1,
        "money":mount,
        "name":wa[0].get_type_display()
    }
    ea = record.filter(type="2")
    mount = 0
    for e in ea:
        mount = mount + e.paymoney
    eall = {
        "num": 2,
        "money": mount,
        "name": ea[0].get_type_display()
    }
    pa = record.filter(type="3")
    mount = 0
    for p in pa:
        mount = mount + p.paymoney
    pall = {
        "num": 3,
        "money": mount,
        "name": pa[0].get_type_display()
    }
    return render(request, "resident/slide/pay.html", {
        "userid": userid,
        "water": water,
        "electricity": electricity,
        "propay": propay,
        "record":record,
        "wall":wall,
        "eall":eall,
        "pall":pall
    })

def payPage(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    paytype = request.POST.get("paytype")
    userid = request.session.get("userId")
    payUser = payment.objects.get(paypeople_id=userid, paytype=paytype)

    return render(request, "resident/slide/payPage.html",
                  {
                      "money": payUser.paysum,
                      "payname": payUser.get_paytype_display()}
                  )

def pay_success(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束

    paytype = request.POST.get("paytype")
    if paytype == "水费":
        paytype = "1"
    if paytype == "电费":
        paytype = "2"
    if paytype == "物业费":
        paytype = "3"
    userid = request.session.get("userId")
    payUser = payment.objects.get(paypeople_id=userid, paytype=paytype)
    record = bill()
    record.type = paytype
    record.paymoney = payUser.paysum
    record.people_id = payUser.paypeople_id
    record.date = datetime.now()
    record.save()
    payUser.paysum = 0
    payUser.paydate = "2099-12-31"
    payUser.save()
    return redirect("/pay/")