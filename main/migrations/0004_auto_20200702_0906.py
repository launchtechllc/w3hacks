# Generated by Django 3.0.7 on 2020-07-02 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200702_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectexercise',
            name='implementation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Implementation'),
        ),
    ]