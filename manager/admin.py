# Register your models here.
from django.contrib import admin
from manager.models import resident, manager, demand, goods, shop, suggestion, worker, payment, plot, newsmessage

admin.site.site_header = '物业管理后台'
admin.site.site_title = '物业管理'
admin.site.index_title= '物业管理'

@admin.register(resident)
class ResidentAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ["rnum","rpassword","rname","rgender","raddress","rtelnum","rwechat","rqq","rbirth","rcontend"]
    # 过滤字段
    list_filter = ['rname']
    # 搜索字段
    search_fields = ['rname']
    # 分页
    list_per_page = 5
    # 添加,修改页属性
    # 属性的先后顺序
    # fields = ['gdate','ggirlnum',  'gname', 'gboynum', 'isDelete']
    # 给属性分组,上下两个不能一起使用

@admin.register(manager)
class ManagerAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["mnum","mname"]
    pass
    # def gender(self):
    #     if self.sgender==0:
    #         return "男"
    #     else:
    #         return "女"
    #
    # def delete(self):
    #     if self.isDelete:
    #         return "是"
    #     else:
    #         return "否"
    #
    # # 修改标签
    # gender.short_description = "性别"
    # list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', delete]
    # list_per_page = 5
    #
    # # 执行动作的位置
    # actions_on_bottom = True
    # actions_on_top = False

@admin.register(demand)
class DemandAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["dnum","dtype","dcontend"]

@admin.register(goods)
class GoodsAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["goodnum","goodname"]

@admin.register(shop)
class ShopAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["id","rnum_id"]

@admin.register(suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["id","scontend","sanswer"]

@admin.register(payment)
class PaymentAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["id","paytype","paypeople_id","paysum"]

@admin.register(plot)
class PlotAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["pnum","pname"]

@admin.register(newsmessage)
class NewsmessageAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["newsnum","newstitle"]

@admin.register(worker)
class WorkerAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["wnum","wname"]