# Generated by Django 2.2.5 on 2020-04-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20200406_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tele',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
