# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0016_navbarentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keynote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(validators=[django.core.validators.RegexValidator('^[a-z]*$', 'Only lower case alphabets are allowed.')], unique=True, max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='event_images/', blank=True)),
                ('venue', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
