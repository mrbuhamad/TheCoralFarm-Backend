# Generated by Django 2.2.7 on 2020-03-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200315_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='item',
        ),
    ]
