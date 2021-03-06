# Generated by Django 2.2.2 on 2019-07-02 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_auto_20190702_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timeToOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 14, 21, 20, 4297), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToSend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 14, 21, 20, 4297), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeFinishOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 14, 21, 20, 4297), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeFood',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 14, 21, 20, 4297), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 14, 21, 20, 4297), null=True),
        ),
    ]
