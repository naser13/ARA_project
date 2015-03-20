# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20150319_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(default=1, to='address.City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(default=1, to='address.Province'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='province',
            field=models.ForeignKey(to='address.Province'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
