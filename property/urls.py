


from django.contrib import admin
from django.conf.urls import url,include
from django.views import static ##新增
from manager import chat_server, views
from property import settings
urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^chat',chat_server.index,name="chat"),
    url(r'^connect/',chat_server.connect,name="connect"),
    url(r'^msg_send/',chat_server.msg_send,name="msg_send"),
    url(r'',include(('manager.urls','resident'),namespace='resident')),

    url(r'^worker/', include(('manager.wurls', 'worker'), namespace='worker')),
    url(r'^manager/', include(('manager.murls', 'managers'), namespace='managers')),
    url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'',views.login),
]

