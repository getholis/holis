# Generated by Django 3.0.5 on 2020-08-08 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20200731_2234'),
        ('chat', '0005_auto_20200726_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('subject', models.CharField(blank=True, max_length=1024, null=True, verbose_name='subject')),
                ('max_users', models.IntegerField(default=0, verbose_name='Max users')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='password')),
                ('service_name', models.CharField(default='conference', max_length=255, verbose_name='Service Name')),
                ('is_public', models.BooleanField(default=True, verbose_name='is public')),
                ('persistent', models.BooleanField(default=True, verbose_name='is public')),
                ('any_can_invite', models.BooleanField(default=True, verbose_name='Any can invite')),
                ('members_only', models.BooleanField(default=False, verbose_name='members only')),
                ('is_one_to_one', models.BooleanField(default=False, verbose_name='is one to one')),
                ('admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL, verbose_name='admins')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='core.Company', verbose_name='company')),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='members')),
                ('outcasts', models.ManyToManyField(related_name='outcats', to=settings.AUTH_USER_MODEL, verbose_name='outcats')),
                ('owners', models.ManyToManyField(related_name='owners', to=settings.AUTH_USER_MODEL, verbose_name='owners')),
            ],
            options={
                'ordering': ['-created'],
                'unique_together': {('name', 'company')},
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField(verbose_name='text')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.Room', verbose_name='channel')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.Company', verbose_name='company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-created'],
                'unique_together': {('id', 'company')},
            },
        ),
        migrations.CreateModel(
            name='MessageAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('attachment', models.FileField(upload_to='', verbose_name='attachment')),
                ('mimetype', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mimetype')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='core.Company', verbose_name='company')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='chat.Message', verbose_name='message')),
            ],
            options={
                'verbose_name': 'message attachment',
                'verbose_name_plural': 'message attachments',
                'ordering': ['created'],
                'unique_together': {('id', 'company')},
            },
        ),
    ]
