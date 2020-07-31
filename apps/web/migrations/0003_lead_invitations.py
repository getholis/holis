# Generated by Django 3.0.5 on 2020-07-16 23:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_lead_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='invitations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254, verbose_name='Email'), default=list, size=None),
        ),
    ]
