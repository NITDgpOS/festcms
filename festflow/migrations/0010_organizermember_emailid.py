# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0009_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizermember',
            name='emailId',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
