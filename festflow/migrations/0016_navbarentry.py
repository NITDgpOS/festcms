# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0015_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.URLField(default='#')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Navbar Entry',
                'verbose_name_plural': 'Navbar Entries',
            },
        ),
    ]
