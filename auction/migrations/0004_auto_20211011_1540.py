# Generated by Django 3.1.5 on 2021-10-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_bider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bider',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=255, max_length=255),
        ),
    ]
