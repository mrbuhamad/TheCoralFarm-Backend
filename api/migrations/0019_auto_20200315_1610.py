# Generated by Django 2.2.7 on 2020-03-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200315_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='coral',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coral',
        ),
        migrations.AddField(
            model_name='order',
            name='coral',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Coral'),
        ),
    ]
