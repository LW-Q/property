# Generated by Django 2.2.5 on 2020-03-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('goodnum', models.IntegerField(primary_key=True, serialize=False)),
                ('goodname', models.CharField(max_length=50, unique=True)),
                ('goodcontend', models.CharField(blank=True, max_length=100, null=True)),
                ('goodtype', models.CharField(blank=True, max_length=50, null=True)),
                ('goodreserve', models.IntegerField(blank=True, null=True, verbose_name='库存')),
                ('goodsale', models.IntegerField(blank=True, null=True, verbose_name='已售')),
                ('goodprice', models.IntegerField(blank=True, null=True)),
                ('beforeprice', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('mnum', models.IntegerField(primary_key=True, serialize=False)),
                ('mpassword', models.CharField(max_length=20)),
                ('mname', models.CharField(blank=True, max_length=20, null=True)),
                ('mtelnum', models.BigIntegerField(blank=True, null=True)),
                ('marea', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='newsmessage',
            fields=[
                ('newsnum', models.AutoField(primary_key=True, serialize=False)),
                ('newsdate', models.DateTimeField(blank=True, null=True)),
                ('newstitle', models.CharField(blank=True, max_length=100, null=True)),
                ('newscontend', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'newsmessage',
                'ordering': ['-newsdate'],
            },
        ),
        migrations.CreateModel(
            name='resident',
            fields=[
                ('rnum', models.IntegerField(primary_key=True, serialize=False)),
                ('rpassword', models.CharField(max_length=20)),
                ('rname', models.CharField(blank=True, max_length=20, null=True)),
                ('rgender', models.CharField(blank=True, choices=[('0', '女'), ('1', '男')], max_length=1, null=True)),
                ('raddress', models.CharField(blank=True, max_length=50, null=True)),
                ('rtelnum', models.BigIntegerField(blank=True, null=True)),
                ('rwechat', models.CharField(blank=True, max_length=20, null=True)),
                ('rqq', models.BigIntegerField(blank=True, null=True)),
                ('rbirth', models.DateField(blank=True, null=True)),
                ('rcontend', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': '业主',
                'verbose_name_plural': '业主',
                'db_table': 'resident',
            },
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('wnum', models.IntegerField(primary_key=True, serialize=False)),
                ('wpassword', models.CharField(max_length=20)),
                ('wname', models.CharField(blank=True, max_length=20, null=True)),
                ('wtype', models.CharField(choices=[('1', '保安'), ('2', '保洁'), ('3', '维修工'), ('4', '清洁绿化'), ('5', '超市')], max_length=1)),
                ('wtasknum', models.IntegerField(blank=True, null=True)),
                ('wtaskmount', models.IntegerField(blank=True, null=True)),
                ('wjoindate', models.DateField(blank=True, null=True)),
                ('wtelnum', models.BigIntegerField(blank=True, null=True)),
                ('wholiday', models.CharField(blank=True, max_length=40, null=True)),
                ('whoursalary', models.IntegerField(blank=True, null=True)),
                ('wskilled', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': '工人',
                'verbose_name_plural': '工人',
                'db_table': 'worker',
            },
        ),
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scontend', models.CharField(max_length=100)),
                ('sanswer', models.CharField(blank=True, max_length=100, null=True)),
                ('sanum', models.IntegerField(blank=True, null=True)),
                ('snum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.resident')),
            ],
            options={
                'verbose_name': '反馈',
                'verbose_name_plural': '反馈',
                'db_table': 'suggestion',
            },
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodmount', models.IntegerField(default=0)),
                ('goodnum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.goods')),
                ('rnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.resident')),
            ],
            options={
                'verbose_name': '业主购物车',
                'verbose_name_plural': '业主购物车',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='plot',
            fields=[
                ('pnum', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(blank=True, max_length=20, null=True)),
                ('pcontend', models.CharField(blank=True, max_length=40, null=True)),
                ('pmnum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.manager')),
            ],
            options={
                'verbose_name': '小区区域',
                'verbose_name_plural': '小区区域',
                'db_table': 'plot',
            },
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paysum', models.IntegerField(default=0)),
                ('paytype', models.CharField(choices=[('1', '水费'), ('2', '电费'), ('3', '物业费')], max_length=1)),
                ('paydate', models.DateField(blank=True, default='2099-12-31', null=True)),
                ('paypeople', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.resident')),
            ],
            options={
                'verbose_name': '缴费信息',
                'verbose_name_plural': '缴费信息',
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='demand',
            fields=[
                ('dnum', models.AutoField(primary_key=True, serialize=False)),
                ('dtype', models.CharField(choices=[('1', '保安'), ('2', '保洁'), ('3', '维修工'), ('4', '清洁绿化'), ('5', '超市')], max_length=1)),
                ('dcontend', models.CharField(blank=True, max_length=100, null=True)),
                ('is_accept', models.BooleanField(blank=True, null=True)),
                ('dwnum', models.IntegerField(blank=True, null=True)),
                ('drnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.resident')),
            ],
            options={
                'verbose_name': '业主需求',
                'verbose_name_plural': '业主需求',
                'db_table': 'demand',
            },
        ),
    ]
