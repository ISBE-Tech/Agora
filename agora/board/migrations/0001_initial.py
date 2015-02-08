# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=300)),
                ('time', models.DateField()),
                ('score', models.SmallIntegerField()),
                ('comments', models.ForeignKey(to='board.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('score', models.SmallIntegerField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('posts', models.ForeignKey(to='board.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
