from django.conf.urls import url, include

from manager import views,market,initdata,pay,service

urlpatterns = [
    # 服务选择
    url(r'^choose', service.choose, name="choose"),
    url(r'^payService', service.payService, name="payService"),
    url(r'^payser_success', service.payser_success, name="payser_success"),
    url(r'^clean/', service.clean, name="clean"),
    url(r'^door/', service.door.as_view(), name="door"),
    url(r'^fault/', service.fault.as_view(), name="fault"),
    url(r'^safe/', service.safe.as_view(), name="safe"),
    url(r'^alldemand/', service.alldemand, name="alldemand"),
    url(r'^changedemand/(\d+)', service.changedemand, name="changedemand"),
    url(r'^change_post/', service.change_post, name="change_post"),
    url(r'^deletede/(\d+)', service.deletede, name="deletede"),
    url(r'^news/$', service.news, name="news"),

    # 居民操作
    url(r'^index/$', views.index, name="index"),
    url(r'^login/$', views.login, name="login"),
    url(r'^changeRe/', views.changeRe, name="changeRe"),
    url(r'^doLogin/$', views.doLogin, name="doLogin"),
    url(r'^Logout/', views.Logout, name="Logout"),
    url(r'^message/', views.message, name="message"),
    url(r'^suggest/', views.suggest, name="suggest"),


    # 超市url
    url(r'^market', market.market, name="market"),
    url(r'^cart', market.cart, name="cart"),
    url(r'^addCart', market.addCart, name="addCart"),
    url(r'^deleteCart', market.deleteCart, name="deleteCart"),
    url(r'^changeCart', market.changeCart, name="changeCart"),
    url(r'buy_success', market.buy_success, name="buy_success"),
    url(r'buyDetail', market.buyDetail, name="buyDetail"),
    url(r'^changeOrder', market.changeOrder, name="changeOrder"),
    url(r'^deleteOrder', market.deleteOrder, name="deleteOrder"),
    url(r'buy', market.buy, name="buy"),
    url(r'^deletebuy', market.deletebuy, name="deletebuy"),
    url(r'^myBuy', market.myBuy, name="myBuy"),

    # 缴费
    url(r'^payPage/', pay.payPage, name="payPage"),
    url(r'^pay_success/', pay.pay_success, name="pay_success"),
    url(r'^pay/$', pay.pay, name="pay"),


    # 数据初始化
    url(r'^createresident/', initdata.createResident),
]
