# Generated by Django 3.0.5 on 2020-07-17 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_lead_invitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Company code'),
        ),
    ]
