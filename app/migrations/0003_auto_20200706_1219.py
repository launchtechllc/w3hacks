# Generated by Django 3.0.7 on 2020-07-06 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200706_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_link',
            new_name='website',
        ),
    ]