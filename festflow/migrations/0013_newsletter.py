# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0012_auto_20161120_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=50, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
