# Generated by Django 3.2 on 2021-07-01 15:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0014_alter_room_last_message_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='last_message_ts',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
