# Generated by Django 3.0.3 on 2020-05-22 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20200522_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 20, 14, 45, 907830)),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 20, 14, 45, 908892)),
        ),
    ]
