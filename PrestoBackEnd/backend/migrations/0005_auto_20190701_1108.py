# Generated by Django 2.2.2 on 2019-07-01 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190701_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='priceBase',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 8, 39, 160748), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToSend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 8, 39, 160748), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeFinishOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 8, 39, 160748), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeFood',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 8, 39, 160748), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 8, 39, 160748), null=True),
        ),
    ]