# Generated by Django 3.1.7 on 2021-03-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='company_code',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='Company code'),
        ),
    ]
