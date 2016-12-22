# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0013_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('identifier', models.CharField(unique=True, max_length=50)),
                ('contact_email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
    ]
