# Generated by Django 3.0.5 on 2020-06-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200502_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='jid',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Jabber ID'),
        ),
    ]
