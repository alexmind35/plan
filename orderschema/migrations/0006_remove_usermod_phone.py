# Generated by Django 3.1.4 on 2020-12-16 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderschema', '0005_auto_20201216_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermod',
            name='phone',
        ),
    ]
