# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0008_auto_20161026_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='sponsor_logos/')),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
    ]
