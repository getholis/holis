# Generated by Django 3.2 on 2021-06-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0009_auto_20210523_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='reads',
            field=models.JSONField(default=dict, verbose_name='reads'),
        ),
    ]
