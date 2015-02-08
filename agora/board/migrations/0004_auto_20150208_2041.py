# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150205_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='posts',
        ),
        migrations.AddField(
            model_name='user',
            name='Posts',
            field=models.ForeignKey(to='board.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
    ]
