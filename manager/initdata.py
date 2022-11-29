

from django.http import HttpResponse, JsonResponse
from manager.models import resident, manager, demand, goods, shop, suggestion, worker, payment, plot, newsmessage, bill, order

def createResident(request):
    man1 = manager(mnum=10001, mpassword=123, mname="一管", mtelnum=13225892862)
    man1.save()
    man2 = manager(mnum=10002, mpassword=123, mname="二管", mtelnum=15896545236)
    man2.save()
    man3 = manager(mnum=10003, mpassword=123, mname="三管", mtelnum=18478562564)
    man3.save()

    plot1 = plot(pnum=1, pname="蔷薇园", pmnum=man1, pcontend="第一楼，最贵的")
    plot1.save()
    plot2 = plot(pnum=2, pname="百合园", pmnum=man2, pcontend="第二楼，最便宜的")
    plot2.save()

    res1 = resident.createResident(13502, "123", "李伟", "1", "蔷薇园3幢502", 13225892862, "tylwl2333", 1017519980,
                                   "1998-06-25", "五室一厅，五百平，一千五百万")
    res1.save()
    res2 = resident.createResident(25302, "123", "没人", "1", "百合园5幢302", 17855962543, "jk520", 165465465, "2008-09-25",
                                   "三室一厅，三百平，五百万")
    res2.save()
    res3 = resident.createResident(16302, "123", "有人", "1", "蔷薇园6幢302", 18855066035, "luoli520", 116565123,
                                   "2006-08-06", "二室一厅，二百平，三百万")
    res3.save()
    res4 = resident.createResident(27101, "123", "坑人", "1", "百合园7幢101", 13866921806, "hello", 87965231, "1985-5-14",
                                   "三室二厅，四百平，一千百万")
    res4.save()
    res5 = resident.createResident(15209, "123", "狠人", "1", "蔷薇园5幢209", 18155054480, "nimei", 687256426, "1990-11-12",
                                   "五室三厅，八百平，五千万")
    res5.save()

    dem1 = demand(dnum=93001, drnum=res1, dtype="3", dcontend="下水道堵了", is_accept=True, dwnum=90003)
    dem1.save()
    dem2 = demand(dnum=91001, drnum=res2, dtype="1", dcontend="有小偷", is_accept=True, dwnum=90001)
    dem2.save()
    dem3 = demand(dnum=92001, drnum=res3, dtype="2", dcontend="帮我家里打扫一下", is_accept=False, dwnum=None)
    dem3.save()
    dem4 = demand(dnum=94001, drnum=res4, dtype="4", dcontend="楼下草坪草长太多了", is_accept=True, dwnum=90004)
    dem4.save()
    dem5 = demand(dnum=95001, drnum=res5, dtype="5", dcontend="买东西", is_accept=False, dwnum=None)
    dem5.save()

    wor1 = worker(wnum=90001, wpassword=123, wname="一工", wtype="1", wtasknum=None, wtaskmount=10,
                  wjoindate="2019-12-16", wholiday="无", whoursalary=120, wskilled="安保")
    wor1.save()
    wor21 = worker(wnum=90021, wpassword=123, wname="二1工", wtype="2", wtasknum=None, wtaskmount=45,
                   wjoindate="2012-12-16", wholiday="无", whoursalary=120, wskilled="日常保洁,深度保洁,厨房保养,卫生间保养",wtelnum=13866587452)
    wor22 = worker(wnum=90022, wpassword=123, wname="二2工", wtype="2", wtasknum=None, wtaskmount=13,
                   wjoindate="2019-12-16", wholiday="无", whoursalary=120, wskilled="日常保洁,深度保洁,厨房保养,卫生间保养",wtelnum=18745621254)
    wor23 = worker(wnum=90023, wpassword=123, wname="二3工", wtype="2", wtasknum=None, wtaskmount=44,
                   wjoindate="2013-01-16", wholiday="无", whoursalary=120, wskilled="擦玻璃，新居开荒，家庭长期保洁",wtelnum=13654785214)
    wor24 = worker(wnum=90024, wpassword=123, wname="二4工", wtype="2", wtasknum=None, wtaskmount=22,
                   wjoindate="2017-11-23", wholiday="无", whoursalary=120, wskilled="擦玻璃，新居开荒，家庭长期保洁",wtelnum=13655887741)

    wor21.save()
    wor22.save()
    wor23.save()
    wor24.save()

    wor31 = worker(wnum=90031, wpassword=123, wname="三1工", wtype="3", wtasknum=None, wtaskmount=50,
                   wjoindate="2017-12-16", wholiday="无", whoursalary=120, wskilled="管道疏通,水龙头更换,马桶维修",wtelnum=15544786601)
    wor32 = worker(wnum=90032, wpassword=123, wname="三2工", wtype="3", wtasknum=None, wtaskmount=21,
                   wjoindate="2020-02-03", wholiday="无", whoursalary=120, wskilled="管道疏通,水龙头更换,马桶维修",wtelnum=16955478546)
    wor33 = worker(wnum=90033, wpassword=123, wname="三3工", wtype="3", wtasknum=None, wtaskmount=35,
                   wjoindate="2013-06-21", wholiday="无", whoursalary=100, wskilled="换窗纱,换锁,灯具安装",wtelnum=17755467744)
    wor34 = worker(wnum=90034, wpassword=123, wname="三4工", wtype="3", wtasknum=None, wtaskmount=14,
                   wjoindate="2017-04-15", wholiday="无", whoursalary=100, wskilled="换窗纱,换锁,灯具安装",wtelnum=16654787451)
    wor35 = worker(wnum=90035, wpassword=123, wname="三5工", wtype="3", wtasknum=None, wtaskmount=46,
                   wjoindate="2014-11-07", wholiday="无", whoursalary=130, wskilled="空调加氟,空调维修",wtelnum=18755226654)
    wor36 = worker(wnum=90036, wpassword=123, wname="三6工", wtype="3", wtasknum=None, wtaskmount=13,
                   wjoindate="2020-03-18", wholiday="无", whoursalary=130, wskilled="空调加氟,空调维修",wtelnum=13955487412)
    wor31.save()
    wor32.save()
    wor33.save()
    wor34.save()
    wor35.save()
    wor36.save()

    wor4 = worker(wnum=90004, wpassword=123, wname="四工", wtype="4", wtasknum=None, wtaskmount=10,
                  wjoindate="2019-12-16", wholiday="无", whoursalary=120, wskilled="绿化")
    wor4.save()
    wor5 = worker(wnum=90005, wpassword=123, wname="五工", wtype="5", wtasknum=None, wtaskmount=10,
                  wjoindate="2019-12-16", wholiday="无", whoursalary=120, wskilled="超市")
    wor5.save()

    sug1 = suggestion(snum=res1, scontend="希望水费低一点", sanswer="", sanum=None)
    sug1.save()

    sug2 = suggestion(snum=res2, scontend="希望电费低一点", sanswer="那是不可能的", sanum=10001)
    sug2.save()
    sug3 = suggestion(snum=res3, scontend="希望有人来帮我买一包盐", sanswer="这里是提建议的，买东西去超市", sanum=10003)
    sug3.save()
    sug4 = suggestion(snum=res4, scontend="希望物业费低一点", sanswer="", sanum=None)
    sug4.save()

    py11 = payment(paysum=52, paytype="1", paypeople=res1, paydate="2020-3-30")
    py12 = payment(paysum=0, paytype="2", paypeople=res1, paydate="2020-3-30")
    py13 = payment(paysum=500, paytype="3", paypeople=res1, paydate="2020-3-30")
    py11.save()
    py12.save()
    py13.save()

    py21 = payment(paysum=44, paytype="1", paypeople=res2, paydate="2020-3-30")
    py22 = payment(paysum=0, paytype="2", paypeople=res2, paydate="2020-3-30")
    py23 = payment(paysum=500, paytype="3", paypeople=res2, paydate="2020-3-30")
    py21.save()
    py22.save()
    py23.save()

    py31 = payment(paysum=0, paytype="1", paypeople=res3, paydate="2020-3-30")
    py32 = payment(paysum=33, paytype="2", paypeople=res3, paydate="2020-3-30")
    py33 = payment(paysum=500, paytype="3", paypeople=res3, paydate="2020-3-30")
    py31.save()
    py32.save()
    py33.save()

    py41 = payment(paysum=213, paytype="1", paypeople=res4, paydate="2020-3-30")
    py42 = payment(paysum=0, paytype="2", paypeople=res4, paydate="2020-3-30")
    py43 = payment(paysum=500, paytype="3", paypeople=res4, paydate="2020-3-30")
    py41.save()
    py42.save()
    py43.save()

    py51 = payment(paysum=0, paytype="1", paypeople=res5)
    py52 = payment(paysum=0, paytype="2", paypeople=res5)
    py53 = payment(paysum=0, paytype="3", paypeople=res5)
    py51.save()
    py52.save()
    py53.save()
    # path = "C:/Users/10175/Desktop/test/Django-Axf/goods.xlsx"
    # df = pd.read_excel(path)
    # data = []
    shop1 = shop(goodnum_id=12, rnum=res1)
    shop2 = shop(goodnum_id=123, rnum=res1)
    shop3 = shop(goodnum_id=4, rnum=res1)
    shop4 = shop(goodnum_id=55, rnum=res2)
    shop5 = shop(goodnum_id=67, rnum=res2)
    shop6 = shop(goodnum_id=32, rnum=res3)
    shop7 = shop(goodnum_id=55, rnum=res5)
    shop8 = shop(goodnum_id=70, rnum=res3)
    shop9 = shop(goodnum_id=234, rnum=res4)
    shop1.save()
    shop2.save()
    shop3.save()
    shop4.save()
    shop5.save()
    shop6.save()
    shop7.save()
    shop8.save()
    shop9.save()
    new1 = newsmessage(
        newsnum=1,
        newsdate="2020-3-9 12:00:00",
        newstitle="“电话女哨兵”守护社区防控第一线",
        newscontend="&nbsp&nbsp&nbsp&nbsp“王老，新年好，我是芙蓉社区新月居委会的工作人员小李，打扰您一下，您最近一个月内和您的家人去过武汉吗？有没有和去过武汉的人群接触过？一封信送到您收到了吗？……自大年初二以来，不知道这是第多少个电话，也许是第1800个也或许是第2200个，芙蓉社区新月居委会社区工作者李洁一个又一个电话传递着温馨，忙碌着，此时钟表指针已指向9点20分。<br/>&nbsp&nbsp&nbsp&nbsp新月居委会辖属常住人口7535户，为做到每一户信息都要摸排，每一家都要宣传到位，实现100%全覆盖、无死角、无遗漏，新月居委会线下采用网格化地毯式入户散发一封信和倡议书外，还利用线上物业管家QQ群、微信群传递信息，李洁利用电话回访的方式就成了第三道线宣传值守。<br/>&nbsp&nbsp&nbsp&nbsp从大年初一起，李洁舍弃与家人的团聚，连夜独自一人冒雪从外地驱车赶回合肥，投身到社区防控战斗中。虽然声音已经沙哑、尽管胳膊和肩膀如针扎的酸痛，但电话铃响的一刹那，永远是热情饱满的声音，没有一丝的疑虑和疲惫。在焦灼紧张的防疫战中，李洁用自己的声音缓解群众焦虑的情绪，送去冬日里一丝暖阳，给群众们吃下一颗颗“定心丸”。<br/>&nbsp&nbsp&nbsp&nbsp这仅仅是芙蓉社区防控疫情的一个缩影。芙蓉社区防控应急指挥小组和六个居委会，近百名奋斗在一线的工作者，舍小家，放弃给年幼的宝宝喂奶、放弃照料生病的孩子、放弃老父亲八十岁生日陪伴......召必来、来必战、战必胜，在这场没有硝烟的战争中，她们用自己的行动谱写着初心和使命的新乐章。<br/>&nbsp&nbsp&nbsp&nbsp“我是一名基层工作者，也是一名普通的党员，我要对得起身上佩戴的这枚党徽”，李洁说完又继续拨起下一个居民电话。"
    )
    new2 = newsmessage(
        newsnum=2,
        newsdate="2020-3-4 12:00:00",
        newstitle="树立参与垃圾分类理念",
        newscontend="&nbsp&nbsp&nbsp&nbsp1月20日，在合肥经开区海恒社区“不忘初心牢记使命”主题教育总结大会上，上映了一场以生活垃圾分类为主题的小品表演。<br/>&nbsp&nbsp&nbsp&nbsp记者在现场了解到，此次生活垃圾分类小品表演由海恒社区康利居委会工作人员以及合肥生活垃圾分类工作人员作内容沟通，经精心打造，才面向海恒社区各职能工作人员上映的。<br/>&nbsp&nbsp&nbsp&nbsp“我们一直在想怎样才能把垃圾分类这个热点宣扬出去，绞尽脑汁最终拍板以小品这样嬉皮的形式逗乐社区工作人员，通过小品表演的形式，将生活垃圾分类艺术化，将四分类垃圾：厨余垃圾、可回收物、其他垃圾和有害垃圾生动形象地展示在社区工作人员眼前。这样不仅便于社区工作人员学习生活垃圾分类知识，也能为日后在社区宣传生活垃圾分类工作打下基础。”合肥经开区生活垃圾分类工作人员在接受采访时表示。<br/>&nbsp&nbsp&nbsp&nbsp只争朝夕，不负韶华，守初心，担使命，既然开展了垃圾分类宣传工作，就要做深做细做实，将垃圾分类切实有效的宣传到位。关于生活垃圾分类的宣传和落实，合肥经开区生活垃圾分类工作小组和康利居委会一直在行动。"
    )
    new3 = newsmessage(
        newsnum=3,
        newsdate="2020-3-6 12:00:00",
        newstitle="社区动态：写春联 剪窗花",
        newscontend="&nbsp&nbsp&nbsp&nbsp日前，瑶海区龙岗开发区琥珀社区在龙湖花园东门广场举办“我们的节日”系列之“写春联、送福袋、迎新贺新春”活动。专业书法老师带领10名小小书法爱好者奋笔疾书，为居民书写春联。社区还安排志愿者将写好的部分春联送到行动不便的困难家庭和残疾人手中。此次活动共书写春联、福字300副，发放福袋300个。"
    )
    new4 = newsmessage(
        newsnum=4,
        newsdate="2020-3-2 12:00:00",
        newstitle="检查保安全 欢乐迎福年 慰问暖人心",
        newscontend="&nbsp&nbsp&nbsp&nbsp本报讯 近日，包河区盛大社区食安办对年夜饭承办单位实施登记，督促其向望湖市场监督管理所申报备案。同时，相关单位组成联合检查组，对相关经营户进行突击检查，护航节日食品安全。（韩沁维 记者 赵俊松）<br/><h3>欢乐迎福年</h3>&nbsp&nbsp&nbsp&nbsp本报讯 近日，蜀山区竹荫里社区开展“欢乐过福年”活动，工作人员采取多种形式大力弘扬传统习俗，把关怀和温暖送到百姓心坎上。（郑婷婷 雨静）<br/><h3>慰问暖人心</h3>&nbsp&nbsp&nbsp&nbsp本报讯 近日，包河区王卫社区开展企退人员春节慰问活动，工作人员以电话、微信、小区公告栏张贴须知等方式，逐一通知企退人员，并采取社区发放、小区设点和上门三种形式进行慰问，把党和政府的关怀和温暖送到了1065名退休人员身边。"
    )
    new1.save()
    new2.save()
    new3.save()
    new4.save()
    return HttpResponse("success")