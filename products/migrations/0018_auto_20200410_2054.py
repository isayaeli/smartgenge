# Generated by Django 3.0.3 on 2020-04-10 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200410_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 20, 54, 26, 307115)),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 20, 54, 26, 308151)),
        ),
    ]
