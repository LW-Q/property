from django.db import models

# Create your models here.
# 管理员
'''
    账号/管理号
    密码
    姓名
    电话
    负责区域
'''
class manager(models.Model):
    mnum = models.IntegerField(primary_key=True)
    mpassword = models.CharField(max_length=20)
    mname = models.CharField(max_length=20,null=True, blank=True)
    mtelnum = models.BigIntegerField(null=True, blank=True)
    marea = models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
        return self.mname
    class Meta:
        db_table = "manager"
        verbose_name = "管理员"
        verbose_name_plural = "管理员"

# 居民
'''
    账号/业主号
    密码
    姓名
    性别
    住址
    电话
    微信
    qq
    生日
    简介
'''
class resident(models.Model):
    gender_chioce = (
        ('0','女'),
        ('1','男')
    )
    # 头像
    # rimage = models.ImageField()
    # blank=true代表可以写入空值，null=true代表默认为空
    #户号
    rnum = models.IntegerField(primary_key=True)
    # 密码
    rpassword = models.CharField(max_length=20)
    # 户主
    rname = models.CharField(max_length=20, null=True, blank=True)
    # 性别
    rgender = models.CharField(max_length=1,null=True,blank=True,choices=gender_chioce)
    # 地址,哪一户
    raddress = models.CharField(max_length=50, null=True, blank=True)
    # 电话
    rtelnum = models.BigIntegerField(null=True, blank=True)
    # 微信
    rwechat = models.CharField(max_length=20, null=True, blank=True)
    # qq
    rqq = models.BigIntegerField(null=True, blank=True)
    # 生日
    rbirth = models.DateField(null=True, blank=True)
    # 户型,多大面积,简要介绍
    rcontend = models.CharField(max_length=100, null=True, blank=True)

    # 是否在线
    is_online = models.BooleanField(default=False)
    class Meta:
        # 数据库表名
        db_table = "resident"
        verbose_name = "业主"
        verbose_name_plural = "业主"

    @classmethod
    def createResident(cls, num, password, name, gender, add, tel, wechat, qq, birth, contend):
        res = cls(rnum=num, rname=name, rpassword=password, rgender=gender, raddress=add, rtelnum=tel, rwechat=wechat, rqq=qq, rbirth=birth, rcontend=contend)
        return res

#工人
'''
    工号
    密码
    当前任务号
    任务完成数量
    入职时间
    请假申请
    评价
'''
class worker(models.Model):
    type_choice = (
        ('1','保安'),
        ('2','保洁'),
        ('3','维修工'),
        ('4','清洁绿化'),
        ('5','超市'),
    )
    wnum = models.IntegerField(primary_key=True)
    wpassword = models.CharField(max_length=20)
    wname = models.CharField(max_length=20,null=True, blank=True)
    wtype = models.CharField(max_length=1,choices=type_choice)
    wtasknum = models.IntegerField(null=True, blank=True)
    wtaskmount = models.IntegerField(null=True, blank=True)
    wjoindate = models.DateField(null=True, blank=True)
    wtelnum = models.BigIntegerField(null=True, blank=True)
    wholiday = models.CharField(max_length=40,null=True, blank=True)
    # 时薪
    whoursalary = models.IntegerField(null=True, blank=True)
    # 主要任务
    wskilled = models.CharField(max_length=50,null=True, blank=True)
    # 是否在线
    is_online = models.BooleanField(default=False)
    class Meta:
        db_table = "worker"
        verbose_name = "工人"
        verbose_name_plural = "工人"

# 楼栋
'''
    楼栋号
    楼栋名
    负责人编号/管理员编号
    楼栋描述
'''
class plot(models.Model):
    pnum = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=20,null=True, blank=True)
    pmnum = models.ForeignKey(manager,on_delete=models.DO_NOTHING)
    pcontend = models.CharField(max_length=40,null=True, blank=True)
    class Meta:
        # 数据库表名,小区名
        db_table = "plot"
        verbose_name = "小区区域"
        verbose_name_plural = "小区区域"

# 业主需求表
'''
    任务号
    业主号
    需求工类型
    需求描述
    是否被接取
    接取工号
'''
class demand(models.Model):
    worker_type = (
        ('1', '保安'),
        ('2', '保洁'),
        ('3', '维修工'),
        ('4', '清洁绿化'),
        ('5', '超市'),
    )
    dnum = models.AutoField(primary_key=True)
    drnum = models.ForeignKey(resident,on_delete=models.CASCADE)
    dtype = models.CharField(max_length=1,choices=worker_type)
    dcontend = models.CharField(max_length=100,null=True, blank=True)
    is_accept = models.BooleanField(null=True, blank=True)
    dwnum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = "demand"
        verbose_name = "业主需求"
        verbose_name_plural = "业主需求"

# 反馈建议
'''
    反馈人编号
    反馈描述
    回复
    回复人编号
'''
class suggestion(models.Model):
    snum = models.ForeignKey(resident,on_delete=models.CASCADE)
    scontend = models.CharField(max_length=100)
    sanswer = models.CharField(max_length=100,null=True, blank=True)
    sanum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'suggestion'
        verbose_name = "反馈"
        verbose_name_plural = "反馈"

# 缴费信息
'''
缴费类型；1水费，2电费，3物业费
缴费金额
缴费人编号
到期时间
'''
class payment(models.Model):
    pay_type = (
        ('1','水费'),
        ('2','电费'),
        ('3','物业费')
    )
    paysum = models.IntegerField(default=0)
    paytype = models.CharField(max_length=1,choices=pay_type)
    paypeople = models.ForeignKey(resident,on_delete=models.CASCADE)
    paydate = models.DateField(null=True, blank=True,default='2099-12-31')
    class Meta:
        db_table = "payment"
        verbose_name = "缴费信息"
        verbose_name_plural = "缴费信息"


class bill(models.Model):
    pay_type = (
        ('1', '水费'),
        ('2', '电费'),
        ('3', '物业费')
    )
    paymoney = models.IntegerField(default=0)
    type = models.CharField(max_length=1,choices=pay_type)
    people = models.ForeignKey(resident,on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = "bill"
        verbose_name = "缴费记录"
        verbose_name_plural = "缴费记录"
# 超市商品
'''
商品编号
商品名称
商品信息
商品价格
'''
class goods(models.Model):
    goodnum = models.IntegerField(primary_key=True)
    # 商品名称
    goodname = models.CharField(max_length=50)
    # 商品简介
    goodcontend = models.CharField(max_length=100,null=True,blank=True)
    # 商品类别
    goodtype = models.CharField(max_length=50,null=True,blank=True)
    # 库存
    goodreserve = models.IntegerField(null=True,blank=True,verbose_name="库存")
    # 已售
    goodsale = models.IntegerField(null=True,blank=True,verbose_name="已售")
    # 商品价格
    goodprice = models.IntegerField(null=True,blank=True)
    # 原价
    beforeprice = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table='goods'
        verbose_name = "商品"
        verbose_name_plural = "商品"



class order(models.Model):
    ordernum = models.AutoField(primary_key=True)
    ordertime = models.DateTimeField(null=True,blank=True)
    resident = models.ForeignKey(resident,on_delete=models.CASCADE)
    address = models.CharField(max_length=50,null=True,blank=True)
    money = models.IntegerField()
    tele = models.BigIntegerField(null=True,blank=True)
    is_pay  = models.BooleanField(default=False)
    is_take = models.BooleanField(default=False)

    worker = models.ForeignKey(worker,on_delete=models.DO_NOTHING,null=True,blank=True)
    is_success = models.BooleanField(default=False)
    class Meta:
        db_table = "order"
        verbose_name = "订单"

# 业主购物车
'''
商品编号
业主编号
'''
class shop(models.Model):
    goodnum = models.ForeignKey(goods,on_delete=models.CASCADE)
    rnum = models.ForeignKey(resident,on_delete=models.CASCADE)
    goodmount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    # 是否购买
    is_buy = models.BooleanField(default=False)
    order= models.ForeignKey(order,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table='shop'
        verbose_name = "业主购物车"
        verbose_name_plural = "业主购物车"


class newsmessage(models.Model):
    newsnum = models.AutoField(primary_key=True)
    newsdate = models.DateTimeField(null=True,blank=True)
    #长度增加到100
    newstitle = models.CharField(max_length=100,null=True,blank=True)
    #长度增加到10000
    newscontend = models.CharField(max_length=10000,null=True,blank=True)
    class Meta:
        db_table = "newsmessage"
        verbose_name = "新闻"
        verbose_name_plural = "新闻"
        ordering = ['-newsdate']

