# Generated by Django 2.2.9 on 2020-07-05 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200703_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 7, 4)),
        ),
    ]
