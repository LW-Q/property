import json

from django.http import HttpResponse
from django.shortcuts import render
from dwebsocket import accept_websocket

def index(request):
    userid = request.session.get("userId")
    username = request.session.get("userName")
    statu = request.session.get("status")
    print(statu)
    if statu == 1:
        wor = request.GET.get("worker")
        print("hello resident")
        return render(request,"resident/chat.html",{"username": username,"id":userid,'otherid':wor})
    else:
        print("hello worker")
        return render(request,"worker/chat.html",{"username": username,"id":userid})

clients={} #创建客户端列表，存储所有在线客户端

# 允许接受ws请求
# 服务器方法，允许接受ws请求
@accept_websocket
def connect(request):
    # 判断是不是ws请求
    userid = ""
    if request.is_websocket():
        userid = str(request.session.get("userId"))
        clients[userid] = request.websocket
        # 判断是否有客户端发来消息，若有则进行处理，
        # 表示客户端与服务器建立链接成功
        while True:
            '''获取消息，线程会阻塞，
            他会等待客户端发来下一条消息,直到关闭后才会返回，当关闭时返回None'''
            message=request.websocket.wait()
            if not message:
                break
            else:
                msg=str(message, encoding = "utf-8")
                print("hello:"+msg)
                if msg == userid:
                    print("客户端链接成功：" + userid)
                    # 第一次进入，返回在线列表和他的id
                    request.websocket.send(
                        json.dumps({"type": 0, "userlist": list(clients.keys()), "userid": userid}).encode("'utf-8'"))
                    # 更新所有人的userlist
                    for client in clients:
                        clients[client].send(json.dumps({"type": 0, "userlist": list(clients.keys()), "user": None}).encode("'utf-8'"))
            # 客户端关闭后从列表删除
    if userid in clients:
        del clients[userid]
        print(userid + "离线")
        # 更新所有人的userlist
        for client in clients:
            clients[client].send(
                json.dumps({"type": 0, "userlist": list(clients.keys()), "user": None}).encode("'utf-8'"))


#消息发送方法
def msg_send(request):
    msg = request.POST.get("txt")
    useridto = request.POST.get("userto")
    useridfrom = request.POST.get("userfrom")
    print("from:"+useridfrom)
    print("to:"+useridto)
    print("msg:"+msg)
    #发来{msg:data,user:user},表示发送聊天信息，
    # user表示要发送至的用户
    # 私聊，对方显示
    clients[useridto].send(json.dumps({"type": 1, "data": {"msg": msg, "user": useridfrom}}).encode('utf-8'))
    # 私聊，自己显示
    clients[useridfrom].send(json.dumps({"type": 1, "data": {"msg": msg, "user": useridfrom}}).encode('utf-8'))
    return HttpResponse(json.dumps({"msg":"success"}))



