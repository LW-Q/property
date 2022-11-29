from django.conf.urls import url

from manager import manager

urlpatterns = [
    url(r'^index/',manager.index,name="index"),
    url(r'^message/',manager.message,name="message"),
    url(r'^Logout/',manager.Logout,name="Logout"),
    url(r'^changeMa/',manager.changeMa,name="changeMa"),
    url(r'^shownews/',manager.shownews,name="shownews"),
    url(r'^addnews/',manager.addnews,name="addnews"),
    url(r'^changenews/',manager.changenews,name="changenews"),
    url(r'^deleteNew/',manager.deleteNew,name="deleteNew"),

    url(r'^allresident/', manager.allresident, name="allresident"),
    url(r'^changeRe/',manager.changeRe,name="changeRe"),
    url(r'^deleteRe/',manager.deleteRe,name="deleteRe"),
    url(r'^addRe/',manager.addRe,name="addRe"),

    url(r'^allworker/', manager.allworker, name="allworker"),
    url(r'^changeWo/',manager.changeWo,name="changeWo"),
    url(r'^deleteWo/',manager.deleteWo,name="deleteWo"),
    url(r'^addWo/',manager.addWo,name="addWo"),

    url(r'^allpayment/', manager.allpayment, name="allpayment"),
    url(r'^changePay/',manager.changePay,name="changePay"),

    url(r'^allsuggestion/', manager.allsuggestion, name="allsuggestion"),
    url(r'^answer/', manager.answer, name="answer"),


]