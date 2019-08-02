# Generated by Django 2.2.2 on 2019-07-30 18:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_auto_20190731_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='onMenu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.OnMenu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 31, 1, 14, 32, 332292), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToSend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 31, 1, 14, 32, 332292), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeFinishOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 31, 1, 14, 32, 331265), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeFood',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 31, 1, 14, 32, 331265), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 31, 1, 14, 32, 331265), null=True),
        ),
    ]
