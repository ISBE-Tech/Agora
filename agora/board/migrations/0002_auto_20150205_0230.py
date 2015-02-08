# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
