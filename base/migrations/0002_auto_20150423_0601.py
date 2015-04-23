# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headmaster',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.RemoveField(
            model_name='headmaster',
            name='id',
        ),
        migrations.RemoveField(
            model_name='headmaster',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AddField(
            model_name='headmaster',
            name='person_ptr',
            field=models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL, default=1, auto_created=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('TE', 'معلم'), ('HM', 'مدیر'), ('ST', 'دانش آموز')], max_length=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='person_ptr',
            field=models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL, default=1, auto_created=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='person_ptr',
            field=models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL, default=1, auto_created=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
