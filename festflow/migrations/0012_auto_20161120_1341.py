# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0011_auto_20161119_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
