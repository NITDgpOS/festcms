# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import festflow.models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0017_keynote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarentry',
            name='url',
            field=models.CharField(max_length=100, default='#', validators=[festflow.models.validate_navbar_entry]),
        ),
    ]
