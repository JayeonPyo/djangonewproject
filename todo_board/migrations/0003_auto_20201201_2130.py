# Generated by Django 2.1 on 2020-12-01 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_board', '0002_auto_20201130_1633'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todolist',
            table='todo_list',
        ),
    ]