# Generated by Django 3.2.8 on 2021-10-17 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
    ]
