# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0014_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('identifier', models.CharField(max_length=50, unique=True)),
                ('question', ckeditor_uploader.fields.RichTextUploadingField()),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
                'verbose_name': 'FAQ',
            },
        ),
    ]
