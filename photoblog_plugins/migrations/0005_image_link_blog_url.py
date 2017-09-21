# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog_plugins', '0004_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_link',
            name='blog_url',
            field=models.CharField(max_length=200, default=datetime.datetime(2017, 9, 20, 11, 22, 34, 874535, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
