# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0007_organizermember_avatar_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizermember',
            name='position',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizermember',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
