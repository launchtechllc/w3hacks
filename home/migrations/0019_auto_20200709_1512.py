# Generated by Django 3.0.7 on 2020-07-09 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200709_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 15, 12, 17, 465304)),
        ),
    ]
