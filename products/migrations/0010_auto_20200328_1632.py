# Generated by Django 3.0.3 on 2020-03-28 13:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200328_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 16, 32, 27, 564331)),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='listed_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Wishlist'),
        ),
        migrations.AlterField(
            model_name='wishlist_item',
            name='updateon',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 16, 32, 27, 565383)),
        ),
    ]
