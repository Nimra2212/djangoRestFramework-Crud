# Generated by Django 3.2.8 on 2021-11-01 18:06

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_task_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(default=django.contrib.auth.models.User, max_length=100),
        ),
    ]
