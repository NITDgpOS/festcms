# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0010_organizermember_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('identifier', models.CharField(unique=True, max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'about',
                'verbose_name': 'about',
            },
        ),
        migrations.AlterField(
            model_name='organizermember',
            name='contactURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
