# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0005_event_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='organizerMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=15)),
                ('contactURL', models.URLField()),
            ],
        ),
    ]
