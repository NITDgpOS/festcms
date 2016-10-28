# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0006_organizermember'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizermember',
            name='avatar_img',
            field=models.ImageField(null=True, upload_to='avatar_images/', blank=True),
        ),
    ]
