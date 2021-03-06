# Generated by Django 2.2.2 on 2019-07-02 06:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20190702_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timeToOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 13, 31, 16, 262672), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToSend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 13, 31, 16, 262672), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeFinishOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 13, 31, 16, 258672), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeFood',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 13, 31, 16, 258672), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 2, 13, 31, 16, 258672), null=True),
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('typeDrinks', models.CharField(choices=[('hot', 'ร้อน'), ('cool', 'เย็น'), ('spin', 'ปั่น')], max_length=20)),
                ('priceBase', models.PositiveIntegerField()),
                ('markets', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Market')),
            ],
        ),
    ]
