# Generated by Django 3.0.7 on 2020-07-09 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200708_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 13, 36, 4, 797643)),
        ),
        migrations.AlterField(
            model_name='newsupdate',
            name='date_posted',
            field=models.DateField(default=datetime.date(2020, 7, 9)),
        ),
    ]