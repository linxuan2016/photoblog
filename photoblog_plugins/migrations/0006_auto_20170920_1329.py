# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog_plugins', '0005_image_link_blog_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_link',
            old_name='blog_url',
            new_name='link_url',
        ),
    ]
