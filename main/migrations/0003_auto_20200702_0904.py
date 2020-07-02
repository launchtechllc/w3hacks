# Generated by Django 3.0.7 on 2020-07-02 16:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_implementation'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectexercise',
            name='implementation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Implementation'),
        ),
        migrations.AlterField(
            model_name='implementation',
            name='type',
            field=models.CharField(choices=[('PL', 'Programming Language'), ('F', 'Framework'), ('L', 'Library'), ('T', 'Tool')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 7, 2)),
        ),
    ]