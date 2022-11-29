# 超市功能

from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from manager.models import resident, manager, demand, goods, shop, suggestion, worker, payment, plot, newsmessage, bill, \
    order

'''
居民超市功能
'''

def market(request):
    # 是否登录
    is_login = request.session.get("is_login")
    if not is_login:
        request.session['is_return'] = True
        request.session.set_expiry(5)
        return redirect("/login/")
    # 判断登录结束
    tp = request.GET.get("type")
    userid = request.session.get("userId")
    # 购物车
    cartAll = shop.objects.filter(rnum__rnum=userid)
    allmoney = 0
    for c in cartAll:
        allmoney = allmoney + c.price
    # 商品
    if tp is None or tp == "all":
        good = goods.objects.all()
    else:
        good = goods.objects.filter(goodtype=tp)
    gtypes = list(goods.objects.values("goodtype"))
    gtype = list()
    for gt in gtypes:
        gtype.append(gt["goodtype"])
    gtypeall = list()
    for gt in gtype:
        try:
            gtypeall.index(gt)
        except:
            gtypeall.append(gt)

    data = {
        "userid": userid,
        "goods": good,
        "goodtypes": gtypeall,
        "carts": cartAll,
        "allmoney": allmoney
    }
    return render(request, "resident/slide/market.html",data)

def cart(request):
    userid = request.session.get("userId")
    ca = shop.objects.filter(rnum__rnum=userid)
    allmoney = 0
    for c in ca:
        allmoney = allmoney + c.price

    return render(request,"resident/slide/cart.html",{"carts":ca,"allmoney":allmoney})

def addCart(request):
    gnum = request.POST.get("num")
    userid = request.session.get("userId")
    mount = int(request.POST.get("mount"))
    gprice = goods.objects.get(goodnum=gnum).goodprice
    print(mount)
    car = shop(goodnum_id=gnum,rnum_id=userid,goodmount=mount,price=mount*gprice)
    car.save()
    return JsonResponse({"result":"ok"})

def deleteCart(request):
    gnum = request.POST.get("num")
    car= shop.objects.get(id=gnum)
    car.delete()
    return JsonResponse({"result":"删除成功"})

def changeCart(request):
    gnum = request.POST.get("num")
    userid = request.session.get("userId")
    mount = int(request.POST.get("mount"))
    car = shop.objects.get(id=gnum,rnum_id=userid)
    gprice = goods.objects.get(goodnum=gnum).goodprice
    car.goodmount = mount
    car.price = mount*gprice
    car.save()
    return JsonResponse({"result":"修改成功"})

def buy(request):
    userid = request.session.get("userId")
    allmoney = request.GET.get("money")
    print(allmoney)
    print("hello1")
    ca = shop.objects.filter(rnum__rnum=userid)
    ret = {
        "now":datetime.now(),
        "cart":ca,
        "money":allmoney
    }
    return render(request,"resident/slide/buy.html",ret)

def deletebuy(request):
    num = request.GET.get("num")
    orde = order.objects.get(ordernum=num)
    orde.delete()
    return redirect("/cart/")

def buy_success(request):
    tele = request.POST.get("tele")
    money = request.POST.get("money")
    address = request.POST.get("address")
    userid = request.session.get("userId")
    print("jin buysuc")
    orde = order()
    orde.address = address
    orde.ordertime = datetime.now()
    orde.tele =tele
    orde.resident_id = userid
    orde.money = money
    orde.is_pay = True
    orde.save()
    print(orde)
    print("orde")
    allGoods = shop.objects.filter(rnum__rnum=userid)
    for g in allGoods:
        g.is_buy = True
        g.order = orde
        g.save()
    print("go mybuy")
    return redirect("/myBuy/")

def myBuy(request):
    userid = request.session.get("userId")
    allorder = order.objects.filter(resident__rnum=userid)
    ret = {"orders": allorder}
    return render(request,"resident/slide/myBuy.html",ret)
def buyDetail(request):
    userid = request.session.get("userId")
    num = request.GET.get("num")
    allGoods = shop.objects.filter(order_id=num)
    orde = order.objects.get(ordernum=num)
    return render(request,"resident/slide/buyDetail.html",{"cart":allGoods,"order":orde})

def changeOrder(request):
    tele = request.POST.get("tele")
    address = request.POST.get("address")
    num = request.POST.get("num")
    orde = order.objects.get(ordernum=num)
    orde.address =address
    orde.tele = tele
    orde.save()
    return redirect("/myBuy/")

def deleteOrder(request):
    num = request.POST.get("num")
    orde = order.objects.get(ordernum=num)
    orde.delete()
    return redirect("/myBuy/")