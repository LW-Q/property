from django.conf.urls import url

from manager import worker

urlpatterns = [
    url(r'^index/',worker.index,name="index"),
    url(r'^message/',worker.message,name="message"),
    url(r'^Logout/',worker.Logout,name="Logout"),
    url(r'^changeWo/',worker.changeWo,name="changeWo"),
    url(r'^alltask/',worker.alltask,name="alltask"),
    url(r'^gettask/(\d+)',worker.gettask,name="gettask"),
    url(r'^showtask/',worker.showtask,name="showtask"),
    url(r'^allMessage/',worker.allMessage,name="allMessage"),

]